from scripts.helpful_scripts import get_account
from brownie import Token, Swap, Contract

def deploy():
    account = get_account()
    token_contract = Token.deploy({"from" : account})

def test_deploy():
    swap = Swap.deploy({"from" : get_account()})
    token = swap.getTokenAddress()
    print("token", token)
    transaction = swap.withdrawMe(1*10**18, {"from" : get_account()})
    transaction.wait(1)
    balance = Token.at(token).balanceOf(swap.address)
    print("balance", balance)

def main():
    test_deploy()