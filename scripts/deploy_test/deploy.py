##deploys charity, treasury and devAndMarketing wallets
from brownie import (
    accounts,
    config,
    network,
    SpiceLiquidityHandler,
    Spice,
    interface,
    Charity,
    Dev,
    Treasury,
    Presale,
)
from scripts.helpful_scripts import get_account
from web3 import Web3
import time

BUSD_ADDRESS = "0x035a87F017d90e4adD84CE589545D4a8C5B7Ec80"
ACCOUNT = get_account()
ROUTER = "0x9Ac64Cc6e4415144C455BD8E4837Fea55603e5c3"
Wallet = "0x8478F8c1d693aB4C054d3BBC0aBff4178b8F1b0B"
OWNER = get_account()


# def deploy_presale():
#     account = get_account()
#     presale = Presale.deploy(Wallet, {"from": account})


def deploy_Contracts():
    account = get_account()
    spice = Spice.deploy(BUSD_ADDRESS, ROUTER, OWNER, {"from": account}, publish_source=True)
    print("deployed spice successfully")



def latest_contract():
    return Spice[-1]




def deploy_liquidity_handler():
    account = get_account()
    spice = Spice[-1]
    pair = spice.pairBusd()
    liquityM = SpiceLiquidityHandler.deploy(
        spice.address, BUSD_ADDRESS, ROUTER, pair, {"from": account}
    )


def set_fee_wallets():
    charity = Charity[-1]
    treasury = Treasury[-1]
    dev = Dev[-1]
    account = get_account()
    spice = Spice[-1]
    presale = Presale[-1]
    liquidity = SpiceLiquidityHandler[-1]
    tx = spice.setFeeReceivers(
        liquidity.address, treasury, charity, dev, {"from": account}
    )
    tx.wait(1)




def main():
    deploy_Contracts()
    # deploy_liquidity_handler()
    # set_fee_wallets()
    