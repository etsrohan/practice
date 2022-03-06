import os
from solcx import compile_standard
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

# Read the solidity file
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Prinitng the solidity file
# print(simple_storage_file)

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.12",
)
# print(compiled_sol)

# Save the Compiled Solidity Code into a file
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# print(abi)
# We choose an HTTP Provider
# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0x363c9a040c11F5A203A9F12803590997C2eB7Aa2"
pvt_key = os.getenv("PRIVATE_KEY")
# print(pvt_key)

# Create a contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)

# Get latest transaction count
nonce = w3.eth.get_transaction_count(my_address)
# print(nonce)

# We need to do the following things:
# 1. Build a transaction
# 2. Sign the transaction
# 3. send the transaction

transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)
# print(transaction)
signed_tx = w3.eth.account.sign_transaction(transaction, private_key=pvt_key)
# Send this signed transaction
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


# Working with the contract, you always need
# 1. Contract Address
# 2. Contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# Call -> Simulate making the call and getting the return value
# Transact -> Actually make a state change

# Initial value of favorite number
print("Initial value of stored number:")
print(simple_storage.functions.retrieve().call())

print("Storing new value...")
nonce += 1
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)
signed_tx = w3.eth.account.sign_transaction(store_transaction, private_key=pvt_key)
send_store_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)

print("New value of stored number:")
print(simple_storage.functions.retrieve().call())
