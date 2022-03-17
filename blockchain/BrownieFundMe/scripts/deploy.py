from brownie import accounts, FundMe, network, config
from scripts.helpful_scripts import get_account, get_aggregator


def deploy_fund_me():
    admin = get_account()
    # Pass the price feed address to our fundme contract

    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        pass

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": admin},
        publish_source=True,
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
