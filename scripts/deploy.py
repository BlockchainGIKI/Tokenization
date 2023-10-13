from scripts.helpfulscripts import get_account
from brownie import Bond, PaymentToken, accounts


def deploy():
    account = get_account()

    print("Deploying Payment Token...")
    payment_token = PaymentToken.deploy(1e9, {"from": account})
    print(f"Payment Token deployed at {payment_token}")

    initialSupply = 1e9
    price = 1000
    fee_rate = 150
    fee_days_interval = 0
    fee_type = "Simple"
    end_time = 0  # should be unix time
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
    print(bond.init_time())
    return bond, payment_token


def main():
    deploy()
