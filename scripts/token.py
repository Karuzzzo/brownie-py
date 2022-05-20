#!/usr/bin/python3

from brownie import DefaultToken, accounts
print('asdfasd')

# NOTE! for verification run: 
# ``` 
# export ETHERSCAN_TOKEN=<etherscan api token> 
# ```

# To connect to real network, run 
# ```
# export WEB3_INFURA_PROJECT_ID=<infura api key>
# ```

def main():
    acct = accounts.load('from_metamask')

    return DefaultToken.deploy("Delete token", "DLT", 1e21, {'from': acct}, publish_source=True)

def verify_existing(address):
    token = DefaultToken.at(address)
    DefaultToken.publish_source(token)

def initial_coin_offering(sender, receiver_list):
    token = main()
    for receiver in receiver_list:
        token.transfer(receiver, 1e16, {'from': sender})


some_addresses = [  "0x72AFAECF99C9d9C8215fF44C77B94B99C28741e8",
                    "0xc929ad75B72593967DE83E7F7Cda0493458261D9",
                    "0x139C8512Cde1778e9b9a8e721ce1aEbd4dD43587"]

initial_coin_offering(sender=accounts.load('from_metamask'), receiver_list=some_addresses)