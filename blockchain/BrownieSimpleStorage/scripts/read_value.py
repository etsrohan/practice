from brownie import SimpleStorage, network, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    # go to the index thats one less than the length (last element)
    # Brownie already knows the ABI & Address
    print(simple_storage.retrieve())


def main():
    read_contract()
