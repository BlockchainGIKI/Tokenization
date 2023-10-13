# from scripts.helpfulscripts import get_account
# from brownie import RemittanceToken, TokenManagement, accounts
# import pytest


# def test_local_integration():
#     # Deploying contracts and setting admins

#     ######### This is for development only #########
#     account = accounts.add(
#         0x9E3B1F1BE5FA36F784064F82EADF0C018CE1CBC835096DFDDAAF6061159C2454
#     )
#     node_account = accounts.add(
#         0x568E078D3AE1C7E1E70A676E9D8A35C7C49E7120777F063555D24709E01326A1
#     )
#     super_admin = accounts.add(
#         0x1A85C269DADE4B03E3C440D213759F9C29F7EF3A1B8AAE88D7270D1E618D4DAC
#     )
#     ######### This is for development only #########

#     # account = get_account()
#     # node_account = get_account(1)
#     # super_admin = get_account(2)
#     rem_token = RemittanceToken.deploy({"from": account})
#     token_management = TokenManagement.deploy(
#         rem_token.address, rem_token.address, {"from": super_admin}
#     )
#     rem_token.transfer(
#         token_management.address, rem_token.totalSupply(), {"from": account}
#     )
#     token_management.setNodeAsAdmin(account, {"from": super_admin})
#     token_management.setNodeAsAdmin(node_account, {"from": super_admin})

#     # Creating customers
#     token_management.createCustomer("Jon Doe", 5000, {"from": account})
#     token_management.createCustomer("Powder Jinx", 1000, {"from": account})
#     token_management.createCustomer("Violet Vi", 1001, {"from": account})
#     token_management.createCustomer("Mercenary", 10000, {"from": account})
#     token_management.createCustomer("Outlander", 6900, {"from": account})
#     token_management.createCustomer("Dark Priest", 416553, {"from": account})
#     token_management.createCustomer("Knight", 52131, {"from": account})
#     token_management.createCustomer("Hui Lee", 5400, {"from": account})
#     token_management.createCustomer("Ren Nark", 1540, {"from": account})
#     token_management.createCustomer("Lo Steelman", 8468, {"from": account})
#     token_management.createCustomer("Cap Prulan", 164654, {"from": account})
#     token_management.createCustomer("Asami Siliconsmith", 69653435, {"from": account})
#     token_management.createCustomer("Chip Sryler", 4160, {"from": account})
#     token_management.createCustomer("An Render", 5646, {"from": account})
#     token_management.createCustomer("Cam Primetime", 780, {"from": account})
#     token_management.createCustomer("Jiao Rowrow", 1200, {"from": account})
#     token_management.createCustomer("Kirone Jell", 65453416, {"from": account})
#     token_management.createCustomer("Perl Booth", 876468, {"from": account})
#     token_management.createCustomer("Aycee Donglemancer", 654354, {"from": account})
#     token_management.createCustomer("Dell Krozhenko", 56468468, {"from": account})

#     # Issuing transactions, setting transaction parameters, and converting tokens
#     tx = token_management.issueTransaction(17, 2, 19, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 17, 2, {"from": account}
#     )
#     token_management.convertTokens(node_account, 19, {"from": account})

#     tx = token_management.issueTransaction(5, 11, 92, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 5, 11, {"from": account}
#     )
#     token_management.convertTokens(node_account, 92, {"from": account})

#     tx = token_management.issueTransaction(4, 10, 43, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 4, 10, {"from": account}
#     )
#     token_management.convertTokens(node_account, 43, {"from": account})

#     tx = token_management.issueTransaction(20, 16, 5, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 20, 16, {"from": account}
#     )
#     token_management.convertTokens(node_account, 5, {"from": account})

#     tx = token_management.issueTransaction(1, 17, 84, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 1, 17, {"from": account}
#     )
#     token_management.convertTokens(node_account, 84, {"from": account})

#     # Deleting Customers
#     token_management.removeCustomer(6, {"from": account})
#     token_management.removeCustomer(9, {"from": account})
#     token_management.removeCustomer(17, {"from": account})

#     # Issuing transactions, setting transaction parameters, and converting tokens
#     tx = token_management.issueTransaction(18, 19, 28, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 18, 19, {"from": account}
#     )
#     token_management.convertTokens(node_account, 28, {"from": account})

#     tx = token_management.issueTransaction(1, 20, 42, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 1, 20, {"from": account}
#     )
#     token_management.convertTokens(node_account, 42, {"from": account})

#     tx = token_management.issueTransaction(1, 13, 49, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 1, 13, {"from": account}
#     )
#     token_management.convertTokens(node_account, 49, {"from": account})

#     tx = token_management.issueTransaction(19, 10, 44, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 19, 10, {"from": account}
#     )
#     token_management.convertTokens(node_account, 44, {"from": account})

#     tx = token_management.issueTransaction(3, 5, 63, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 3, 5, {"from": account}
#     )
#     token_management.convertTokens(node_account, 63, {"from": account})

#     # Creating Customers
#     token_management.createCustomer("Oriana Clicker", 4912, {"from": account})
#     token_management.createCustomer("Akihiko Solave", 5149, {"from": account})
#     token_management.createCustomer("Ayako O'os", 4999, {"from": account})
#     token_management.createCustomer("Mercenary", 7342, {"from": account})
#     token_management.createCustomer("Outlander", 7280, {"from": account})

#     # Issuing transactions, setting transaction parameters, and converting tokens
#     tx = token_management.issueTransaction(12, 10, 91, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 12, 10, {"from": account}
#     )
#     token_management.convertTokens(node_account, 91, {"from": account})

#     tx = token_management.issueTransaction(22, 18, 31, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 22, 18, {"from": account}
#     )
#     token_management.convertTokens(node_account, 31, {"from": account})

#     tx = token_management.issueTransaction(5, 21, 47, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 5, 21, {"from": account}
#     )
#     token_management.convertTokens(node_account, 47, {"from": account})

#     tx = token_management.issueTransaction(4, 20, 23, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 4, 20, {"from": account}
#     )
#     token_management.convertTokens(node_account, 23, {"from": account})

#     tx = token_management.issueTransaction(5, 14, 30, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 5, 14, {"from": account}
#     )
#     token_management.convertTokens(node_account, 30, {"from": account})

#     # Deleting Customers
#     token_management.removeCustomer(13, {"from": account})
#     token_management.removeCustomer(21, {"from": account})
#     token_management.removeCustomer(4, {"from": account})

#     # Issuing transactions, setting transaction parameters, and converting tokens
#     tx = token_management.issueTransaction(15, 24, 7, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 15, 24, {"from": account}
#     )
#     token_management.convertTokens(node_account, 7, {"from": account})

#     tx = token_management.issueTransaction(2, 24, 83, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 2, 24, {"from": account}
#     )
#     token_management.convertTokens(node_account, 83, {"from": account})

#     tx = token_management.issueTransaction(8, 14, 38, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 8, 14, {"from": account}
#     )
#     token_management.convertTokens(node_account, 38, {"from": account})

#     tx = token_management.issueTransaction(25, 8, 234, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 25, 8, {"from": account}
#     )
#     token_management.convertTokens(node_account, 234, {"from": account})

#     tx = token_management.issueTransaction(20, 11, 43, {"from": account})
#     token_management.setTransactionParameters(
#         tx.txid, tx.timestamp, tx.gas_used, 20, 11, {"from": account}
#     )
#     token_management.convertTokens(node_account, 43, {"from": account})

#     # For Customer with account number 3
#     # Checking customer balance and number of transactions
#     assert token_management.getCustomer(3, {"from": account})["balance"] == 1001 - 63
#     assert (
#         token_management.getCustomer(3, {"from": account})["number_of_rem_transactions"]
#         == 1
#     )
#     assert (
#         token_management.getCustomer(3, {"from": account})["number_of_ben_transactions"]
#         == 0
#     )
#     # Checking customer remittance transaction history
#     assert token_management.getRemitTransactionHistory(3, {"from": account})[0][4] == 63
#     assert (
#         token_management.getRemitTransactionHistory(3, {"from": account})[0][1]
#         == "Outlander"
#     )

#     # For Customer with account number 8
#     # Checking customer balance and number of transactions
#     assert (
#         token_management.getCustomer(8, {"from": account})["balance"] == 5400 - 38 + 234
#     )
#     assert (
#         token_management.getCustomer(8, {"from": account})["number_of_rem_transactions"]
#         == 1
#     )
#     assert (
#         token_management.getCustomer(8, {"from": account})["number_of_ben_transactions"]
#         == 1
#     )
#     # Checking customer remittance transaction history
#     assert token_management.getRemitTransactionHistory(8, {"from": account})[0][4] == 38
#     assert (
#         token_management.getRemitTransactionHistory(8, {"from": account})[0][1]
#         == "An Render"
#     )
#     # Checking cusotmer receive transaction history
#     assert (
#         token_management.getReceiveTransactionHistory(8, {"from": account})[0][4] == 234
#     )
#     assert (
#         token_management.getReceiveTransactionHistory(8, {"from": account})[0][0]
#         == "Outlander"
#     )

#     # For Customer with account number 19
#     # Checking customer balance and number of transactions
#     assert (
#         token_management.getCustomer(19, {"from": account})["balance"]
#         == 654354 - 44 + 28
#     )
#     assert (
#         token_management.getCustomer(19, {"from": account})[
#             "number_of_rem_transactions"
#         ]
#         == 1
#     )
#     assert (
#         token_management.getCustomer(19, {"from": account})[
#             "number_of_ben_transactions"
#         ]
#         == 1
#     )
#     # Checking customer remittance transaction history
#     assert (
#         token_management.getRemitTransactionHistory(19, {"from": account})[0][4] == 44
#     )
#     assert (
#         token_management.getRemitTransactionHistory(19, {"from": account})[0][1]
#         == "Lo Steelman"
#     )
#     # Checking cusotmer receive transaction history
#     assert (
#         token_management.getReceiveTransactionHistory(19, {"from": account})[0][4] == 28
#     )
#     assert (
#         token_management.getReceiveTransactionHistory(19, {"from": account})[0][0]
#         == "Perl Booth"
#     )

#     # Checking deleted account numbers
#     token_management.getDeletedAccountNumbers({"from": account}) == (
#         6,
#         9,
#         17,
#         13,
#         21,
#         4,
#     )

#     # Checking transaction hash of the latest transaction
#     tx_number = (
#         token_management.getCustomer(20, {"from": account})[
#             "number_of_rem_transactions"
#         ]
#         - 1
#     )
#     assert (
#         token_management.getTransaction(20, True, tx_number, {"from": account})[
#             "tx_hash"
#         ]
#         == tx.txid
#     )

#     # Checking number of tokens
#     assert (
#         rem_token.balanceOf(node_account)
#         == (
#             (19 + 92 + 43 + 5 + 84)
#             + (28 + 42 + 49 + 44 + 63)
#             + (91 + 31 + 47 + 23 + 30)
#             + (7 + 83 + 38 + 234 + 43)
#         )
#         * 1664
#     )
