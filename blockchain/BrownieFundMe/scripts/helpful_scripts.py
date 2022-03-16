from brownie import network, config, accounts


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"].split(",")[0])


def get_aggregator():
    """
    If we are on a persistent network like rinkeby, use the associated addresses
    otherwise, deploy mocks
    """
    if network.show_active() == "development":
        return None
    else:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
