from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    # account = accounts[0]
    # account = accounts.load("rohan-test-account")
    # print(account)
    # account = accounts.add(config["wallets"]["from_key"].split(",")[0])
    # account2 = accounts.add(config["wallets"]["from_key"].split(",")[1])
    # print(account)
    # print(account2)

    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
