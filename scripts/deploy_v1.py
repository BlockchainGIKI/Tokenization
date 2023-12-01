from scripts.helpfulscripts import get_account
from brownie import Bond_v1, PaymentToken, chain
from datetime import datetime
import time
import csv


def deploy():
    account = get_account()
    # initialSupply = 16.5e6
    # price = 1000
    # fee_rate = 55
    # fee_days_interval = 1  # should be 90 for actual deployment
    # fee_type = "Simple"
    # end_time = int(
    #     datetime(2023, 12, 2, 16, 52).timestamp()
    # )  # should be (2028, 11, 1, 0, 0) for actual deployment

    # print("Deploying Payment Token...")
    # payment_token = PaymentToken.deploy(1e18, {"from": account})
    # # payment_token = PaymentToken[-1]
    # print("Deploying Bond...")
    # bond = Bond_v1.deploy(
    #     initialSupply,
    #     payment_token.address,
    #     price,
    #     fee_rate,
    #     fee_days_interval,
    #     fee_type,
    #     end_time,
    #     {"from": account},
    # )

    # # bond = Bond_v1[-1]
    # # payment_token = PaymentToken[-1]
    # # Adding user
    # add_tx = bond.addUser(account.address, "John", {"from": account})
    # add_tx.wait(1)

    # # Starting the bond issuance process
    # start_tx = bond.start({"from": account})
    # start_tx.wait(1)

    # # User approving bond smart contract to spend tokens on their behalf
    # approve_tx = payment_token.approve(bond.address, 1e9, {"from": account})
    # approve_tx.wait(1)
    # # chain.sleep(86400 * 2)
    # # chain.mine(1)
    # time.sleep(2 * 60 + 30)
    bond = Bond_v1[-1]
    payment_token = PaymentToken[-1]
    bond.pause({"from": account})
    bond.unpause({"from": account})
    print(bond)

    print(bond.getPrice())
    # Buying bonds
    buy_tx = bond.buy(2, {"from": account})
    buy_tx.wait(1)
    print(payment_token.balanceOf(bond))

    # Withdrawing capital generated by issuing bonds
    withdraw_tx = bond.withdraw(1, {"from": account})
    withdraw_tx.wait(1)

    # Enabling users to get paid
    print(bond.bond_state())
    print(bond.end_time())
    print(bond.getTime())
    enable_tx = bond.enableInterest({"from": account})
    enable_tx.wait(1)

    # Paying interest payments
    print(payment_token.balanceOf(bond))
    pay_tx = bond.payInterest({"from": account})
    pay_tx.wait(1)
    print(payment_token.balanceOf(bond))

    # header = ['Name', 'Tx Hash']
    # data = [[]]
    # with open('TX_HASH.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)

    #     # write the header
    #     writer.writerow(header)

    #     # write the data
    #     writer.writerow(data)


# 0xd25190a68016a74d836189a3ef41b32b405efa9ec0271f429f99dc84e5a7d18d
# 0x473a78a3a2da27dc536882498c811584afe44a8019defb0d852c3612f877f8df
def main():
    deploy()