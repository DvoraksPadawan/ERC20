from brownie import network, accounts, config

def get_account(account_index = 0):
    if (network.show_active() == "development"):
        return accounts[account_index]
    if (network.show_active() == "sepolia"):
        return accounts.add(config["wallets"]["account1"])