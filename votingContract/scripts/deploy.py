from brownie import votingContract, accounts, network, config, MockV3Aggregator
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, deploy_mocks
from web3 import Web3

def deploy_voting_contract():
    account = get_account()
    
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        priceFeed = config(["networks"][network.show_active()]["eth_usd_price_feed"])
    else:
        deploy_mocks()
        priceFeed = MockV3Aggregator[-1].address
    
    tx_vote = votingContract.deploy(priceFeed, {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))

    print(f"Transaction deployed to {tx_vote.address}")
    return tx_vote


def main():
    deploy_voting_contract()