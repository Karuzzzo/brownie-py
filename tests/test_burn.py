#!/usr/bin/python3

import brownie

def test_burn(token, accounts):
    before = token.balanceOf(accounts[0])
    burnAmount = 10 ** 17
    token.burn(burnAmount, {'from': accounts[0]})

    assert token.balanceOf(accounts[0]) == (before - burnAmount)

def test_burn_too_much(token, accounts):
    burnAmount = 10 ** 30
    with brownie.reverts():
        token.burn(burnAmount, {'from': accounts[0]})

def test_returns_none(token, accounts):
    tx = token.burn(10**19, {'from': accounts[0]})

    assert tx.return_value is None

def test_burn_unallowed(token, accounts):
    burnAmount = 10 ** 17
    with brownie.reverts():
        token.burnFrom(accounts[1], burnAmount, {'from': accounts[0]})

def test_burn_too_much_unallowed(token, accounts):
    burnAmount = 10 ** 30
    with brownie.reverts():
        token.burnFrom(accounts[1], burnAmount, {'from': accounts[0]})

def test_burn_allowed(token, accounts):
    before = token.balanceOf(accounts[0])
    burnAmount = 10 ** 17

    token.approve(accounts[1], burnAmount, {'from': accounts[0]})

    token.burnFrom(accounts[0], burnAmount, {'from': accounts[1]})
    assert token.balanceOf(accounts[1]) == 0
    # Burned at account 0
    assert token.balanceOf(accounts[0]) == (before - burnAmount)


def test_burn_transferred(token, accounts):
    burnAmount = 10 ** 17

    token.approve(accounts[1], burnAmount, {'from': accounts[0]})
    token.transferFrom(accounts[0], accounts[1], burnAmount, {'from': accounts[1]})
    # Did not approve, all was transferred
    with brownie.reverts():
        token.burnFrom(accounts[0], burnAmount, {'from': accounts[1]})
    assert token.balanceOf(accounts[1]) == burnAmount

def test_burn_twice(token, accounts):
    before = token.balanceOf(accounts[0])
    burnAmount = 10 ** 17

    token.approve(accounts[1], burnAmount, {'from': accounts[0]})
    token.burnFrom(accounts[0], burnAmount, {'from': accounts[1]})
    # ALready burned
    with brownie.reverts():
        token.burnFrom(accounts[0], burnAmount, {'from': accounts[1]})
    assert token.balanceOf(accounts[0]) == (before - burnAmount)

