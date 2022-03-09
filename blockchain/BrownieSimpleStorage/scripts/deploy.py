from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    # --------------------------------------------------------------------
    # account = accounts[0]
    # account = accounts.load("rohan-test-account")
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"].split(",")[0])
    # account2 = accounts.add(config["wallets"]["from_key"].split(",")[1])
    # print(account)
    # print(account2)
    # --------------------------------------------------------------------

    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"].split(",")[0])


def main():
    deploy_simple_storage()
