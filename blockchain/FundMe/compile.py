from solcx import compile_source
import solcx

with open("FundMe.sol", "r") as fo:
    x = compile_source(
        fo.read(),
        allow_paths=[
            "/home/rohan/node_modules/@chainlink/contracts/src/v0.8/interfaces/",
            "/home/rohan/node_modules/@openzeppelin/contracts/token/ERC20/",
        ],
    )

print("Success")
print(x.keys())
print(
    x[
        "/home/rohan/node_modules/@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol:AggregatorV3Interface"
    ].keys()
)
