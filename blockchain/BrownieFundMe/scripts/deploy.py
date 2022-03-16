from brownie import accounts, FundMe, network, config
from scripts.helpful_scripts import get_account, get_aggregator


def deploy_fund_me():
    admin = get_account()
    # Pass the price feed address to our fundme contract

    fund_me = FundMe.deploy(
        get_aggregator(),
        {"from": admin},
        publish_source=True,
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
