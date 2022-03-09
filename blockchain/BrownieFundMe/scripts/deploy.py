from brownie import accounts, FundMe, network, config
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    admin = get_account()
    fund_me = FundMe.deploy({"from": admin})
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
