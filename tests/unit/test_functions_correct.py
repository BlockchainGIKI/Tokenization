from scripts.helpfulscripts import get_account
from scripts.deploy import deploy
from brownie import Bond, PaymentToken, exceptions, chain
import pytest
from datetime import datetime


def test_user_should_not_exist():
    # Arrange
    account = get_account()
    (bond, payment_token) = deploy()

    # Assert
    assert bond.userExists(account) == False


def test_can_add_user():
    # Arrange
    account = get_account()
    account1 = get_account(1)
    (bond, payment_token) = deploy()

    # Act
    bond.addUser(account, "John Doe", {"from": account})
    # Assert
    assert bond.addressToUser(account)[0] == "John Doe"
    assert bond.addressToUser(account)[1] == True
    with pytest.raises(exceptions.VirtualMachineError):
        bond.addUser(account, "John Doe", {"from": account})
    with pytest.raises(exceptions.VirtualMachineError):
        bond.addUser(account1, "John Doe", {"from": account1})


def test_can_remove_users():
    # Arrange
    account = get_account()
    account1 = get_account(1)
    (bond, payment_token) = deploy()

    # Act
    bond.addUser(account, "John Doe", {"from": account})
    bond.removeUser(account, {"from": account})

    # Assert
    assert bond.addressToUser(account)[0] == "John Doe"
    assert bond.addressToUser(account)[1] == False
    with pytest.raises(exceptions.VirtualMachineError):
        bond.removeUser(account, {"from": account})
    with pytest.raises(exceptions.VirtualMachineError):
        bond.removeUser(account1, {"from": account1})


def test_can_get_price():
    # Arrange
    account = get_account()
    initialSupply = 1e9
    price = 1000
    fee_rate = 150
    fee_days_interval = 6
    fee_type = "Compound"
    end_time = int(datetime(2023, 10, 30, 12, 0).timestamp())

    print("Deploying Payment Token...")
    payment_token = PaymentToken.deploy(1e9, {"from": account})
    print("Deploying Bond...")

    # Act
    bond = Bond.deploy(
        initialSupply,
        payment_token.address,
        price,
        fee_rate,
        fee_days_interval,
        fee_type,
        end_time,
        {"from": account},
    )
    bond.start()
    chain.sleep(86400 * 14)
    chain.mine(1)

    print(bond.fee_type())
    print(f"Initial time: {bond.init_time()}")
    print(f"Current time: {bond.getTime()}")
    print(f"End Time: {bond.end_time()}")
    bond.getPrice()
    print(bond.fee_type())
    # Assert
    # assert bond.getPrice() == bond.price()
    # assert bond.getPrice() == price + ((price * fee_days_interval * fee_rate) / 1000)
    assert bond.getPrice() == price * ((1000 + fee_rate) ** 2 / 1000**2)


def test_can_start():
    # Arrange
    account = get_account()
    account1 = get_account(1)
    (bond, payment_token) = deploy()

    # Act
    bond.start({"from": account})

    # Assert
    assert bond.bond_state() == 1


def test_can_set_end_time():
    # Arrange
    account = get_account()
    account1 = get_account(1)
    initialSupply = 1e9
    price = 1000
    fee_rate = 150
    fee_days_interval = 7
    fee_type = "Compound"
    end_time = int(datetime(2023, 10, 30, 12, 0).timestamp())

    print("Deploying Payment Token...")
    payment_token = PaymentToken.deploy(1e9, {"from": account})
    print("Deploying Bond...")

    bond = Bond.deploy(
        initialSupply,
        payment_token.address,
        price,
        fee_rate,
        fee_days_interval,
        fee_type,
        end_time,
        {"from": account},
    )
    bond.start({"from": account})

    # Act
    bond.setEnd(1697444760, {"from": account})

    # Assert
    assert bond.end_time() == 1697444760
    with pytest.raises(exceptions.VirtualMachineError):
        bond.setEnd(1697444760, {"from": account1})
    with pytest.raises(exceptions.VirtualMachineError):
        bond.setEnd(16974447600, {"from": account})


def test_can_pause():
    # Arrange
    account = get_account()
    account1 = get_account(1)
    (bond, payment_token) = deploy()

    # Act
    bond.start({"from": account})
    bond.pause({"from": account})

    # Assert
    assert bond.bond_state() == 2
    with pytest.raises(exceptions.VirtualMachineError):
        bond.pause({"from": account1})


def test_can_unpause():
    # Arrange
    account = get_account()
    account1 = get_account(1)
    (bond, payment_token) = deploy()

    # Act
    bond.start({"from": account})
    bond.pause({"from": account})
    bond.unpause({"from": account})

    # Assert
    assert bond.bond_state() == 1
    with pytest.raises(exceptions.VirtualMachineError):
        bond.pause({"from": account1})


def test_can_buy():
    # Arrange
    account = get_account()
    account1 = get_account(1)
    (bond, payment_token) = deploy()

    # Act
    bond.addUser(account, "John Doe", {"from": account})
    bond.start({"from": account})
    amount = 1
    payment_token.approve(bond.address, amount * bond.getPrice(), {"from": account})
    bond.buy(amount, {"from": account})

    # Assert
    assert bond.getBalance(account) == amount  # * bond.getPrice()
    assert payment_token.balanceOf(account) == 1e9 - amount * bond.getPrice()
    with pytest.raises(exceptions.VirtualMachineError):
        bond.buy(amount, {"from": account})
    with pytest.raises(exceptions.VirtualMachineError):
        bond.buy(amount, {"from": account1})


def test_can_withdraw():
    # Arrange
    account = get_account()
    account1 = get_account(1)
    (bond, payment_token) = deploy()

    # Act
    bond.addUser(account, "John Doe", {"from": account})
    bond.start({"from": account})
    amount = 10
    payment_token.approve(bond.address, amount * bond.getPrice(), {"from": account})
    bond.buy(amount, {"from": account})
    bond.pause({"from": account})
    bond.withdraw(1, {"from": account})

    # Assert
    assert payment_token.balanceOf(bond) == amount * bond.getPrice() - 1
    assert payment_token.balanceOf(account) == 1e9 - amount * bond.getPrice() + 1
    with pytest.raises(exceptions.VirtualMachineError):
        bond.withdraw(1, {"from": account1})
    with pytest.raises(exceptions.VirtualMachineError):
        bond.withdraw(amount * bond.getPrice(), {"from": account})


def test_can_enable_cash_out():
    # Arrange
    account = get_account()
    account1 = get_account(1)
    initialSupply = 100
    price = 1000
    fee_rate = 150
    fee_days_interval = 1
    fee_type = "Compound"
    end_time = int(datetime(2023, 10, 18, 12, 30).timestamp())

    print("Deploying Payment Token...")
    payment_token = PaymentToken.deploy(1e9, {"from": account})
    print("Deploying Bond...")

    bond = Bond.deploy(
        initialSupply,
        payment_token.address,
        price,
        fee_rate,
        fee_days_interval,
        fee_type,
        end_time,
        {"from": account},
    )
    bond.start({"from": account})
    bond.addUser(account.address, "John", {"from": account})
    payment_token.approve(bond.address, 1e9, {"from": account})

    # Act
    chain.sleep(86400 * 2)
    chain.mine(1)
    bond.buy(100, {"from": account})
    bond.enableCashOut({"from": account})

    # Assert
    assert bond.bond_state() == 3
    with pytest.raises(exceptions.VirtualMachineError):
        bond.enableCashOut({"from": account1})


def test_can_cash_out():
    # Arrange
    account = get_account()
    account1 = get_account(1)
    initialSupply = 100
    price = 1000
    fee_rate = 150
    fee_days_interval = 1
    fee_type = "Compound"
    end_time = int(datetime(2023, 10, 18, 12, 30).timestamp())

    print("Deploying Payment Token...")
    payment_token = PaymentToken.deploy(1e9, {"from": account})
    print("Deploying Bond...")

    bond = Bond.deploy(
        initialSupply,
        payment_token.address,
        price,
        fee_rate,
        fee_days_interval,
        fee_type,
        end_time,
        {"from": account},
    )
    bond.start({"from": account})
    bond.addUser(account.address, "John", {"from": account})
    payment_token.approve(bond.address, 1e9, {"from": account})
    chain.sleep(86400 * 2)
    chain.mine(1)
    bond.buy(100, {"from": account})
    bond.enableCashOut({"from": account})

    # Act
    bond.cashOut({"from": account})

    # Assert
    assert payment_token.balanceOf(account) == 1e9
    with pytest.raises(exceptions.VirtualMachineError):
        bond.cashOut({"from": account1})
