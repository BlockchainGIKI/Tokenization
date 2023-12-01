from scripts.helpfulscripts import get_account
from brownie import Bond, PaymentToken, accounts, chain
from datetime import datetime


def deploy():
    account = get_account()

    print("Deploying Payment Token...")
    payment_token = PaymentToken.deploy(1e9, {"from": account})
    print(f"Payment Token deployed at {payment_token}")

    initialSupply = 1e18
    price = 1000
    fee_rate = 150
    fee_days_interval = 1
    fee_type = "Simple"
    end_time = int(datetime(2023, 11, 23, 16, 5).timestamp())
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
    print(f"Bond deployed at {bond.address}")
    # bond.start()

    # print(f"Initial time: {bond.init_time()}")
    # print(f"Current time: {bond.getTime()}")
    # print(f"End Time: {bond.end_time()}")

    # print(bond.getPrice())

    # bond.addUser(account.address, "John", {"from": account})
    # print(bond.addressToUser(account)[0])

    # account1 = get_account(1)
    # payment_token.approve(bond.address, 1e9, {"from": account})
    # # bond.transfer(account, 100, {"from": account})
    # bond.buy(1, {"from": account})
    # print(bond.getBalance(account.address))

    return bond, payment_token


def main():
    deploy()
