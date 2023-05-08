from scripts.helpful_scripts import get_account
from brownie import Token, Swap, Contract, exceptions
import pytest

def test_deploy():
    starting_balance = 10*10**18
    swap = Swap.deploy(starting_balance, {"from" : get_account()})
    token = swap.getTokenAddress()
    withdrawed_balance = 1*10**18
    transaction = swap.withdrawMe(withdrawed_balance, {"from" : get_account()})
    transaction.wait(1)
    balance = Token.at(token).balanceOf(swap.address)
    assert balance == starting_balance - withdrawed_balance
    balance = Token.at(token).balanceOf(get_account())
    assert balance == withdrawed_balance

def test_interaction():
    starting_balance = 10*10**18
    swap = Swap.deploy(starting_balance, {"from" : get_account()})
    contract = Contract.deploy({"from" : get_account()})
    token = swap.getTokenAddress()
    withdrawed_balance = 1*10**18
    transaction = contract.getFunds(withdrawed_balance, swap.address)
    #transaction = swap.withdrawMe(withdrawed_balance, {"from" : get_account()})
    transaction.wait(1)
    balance = Token.at(token).balanceOf(contract.address)
    assert balance == withdrawed_balance
    balance = Token.at(token).balanceOf(swap.address)
    assert balance == starting_balance - withdrawed_balance

def test_allowance_goes_wrong():
    starting_balance = 10*10**18
    swap = Swap.deploy(starting_balance, {"from" : get_account()})
    contract = Contract.deploy({"from" : get_account()})
    token = swap.getTokenAddress()
    withdrawed_balance = 2*10**18
    transaction = contract.getFunds(withdrawed_balance, swap.address)
    #transaction = swap.withdrawMe(withdrawed_balance, {"from" : get_account()})
    transaction.wait(1)
    donated_balance = 1*10**18
    with pytest.raises(exceptions.VirtualMachineError):
        transaction = contract.donate(donated_balance, swap.address)
    transaction.wait(1)

def test_allowance():
    starting_balance = 10*10**18
    swap = Swap.deploy(starting_balance, {"from" : get_account()})
    contract = Contract.deploy({"from" : get_account()})
    token = swap.getTokenAddress()
    withdrawed_balance = 2*10**18
    transaction = contract.getFunds(withdrawed_balance, swap.address)
    #transaction = swap.withdrawMe(withdrawed_balance, {"from" : get_account()})
    transaction.wait(1)
    donated_balance = 1*10**18
    transaction = contract.approve(donated_balance, swap.address, token, {"from" : get_account()})
    transaction.wait(1)
    transaction = contract.donate(donated_balance, swap.address)
    transaction.wait(1)
    balance = Token.at(token).balanceOf(contract.address)
    assert balance == withdrawed_balance - donated_balance
    balance = Token.at(token).balanceOf(swap.address)
    assert balance == starting_balance - withdrawed_balance + donated_balance


