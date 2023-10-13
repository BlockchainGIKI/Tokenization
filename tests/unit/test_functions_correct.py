from scripts.helpfulscripts import get_account
from scripts.deploy import deploy
from brownie import Bond, PaymentToken, exceptions
import pytest


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
    fee_days_interval = 7
    fee_type = "Compound"
    end_time = 1697176800  # should be unix time

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

    # Assert
    assert bond.getPrice() == bond.price()
