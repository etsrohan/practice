// SPDX-License-Identifier: MIT
// Note: We need to deploy this on the testnet. Here we are using the Rinkeby TestNet.

pragma solidity >=0.6.6 <0.9.0;

import "/home/rohan/node_modules/@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe{
    // Mapping of Addresses to Value
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;

    modifier onlyOwner {
        require(msg.sender == owner, "Only the Owner can withdraw the money!");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    // Function that can accept payment
    function fund() public payable {
        // $50 Minimum threshold
        uint256 minimumUSD = 50 * 10 ** 18;
        // what the ETH -> USD confersion rate is
        // Use a decentralized oracle network - Chainlink
        require(getConversionRate(msg.value) > minimumUSD, "You need to spend more ETH!");
        addressToAmountFunded[msg.sender] += msg.value;
        // Add funder to funders array
        funders.push(msg.sender);
    }

    // Get version function calling version function in the interface from
    // AggregatorV3Interface.sol
    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }

    function getPrice() public view returns(uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);

        // Answer returns price of ETH in USD with 8 decimal places
        ( , int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer * 10 ** 10); // Getting Price of ETH in USD with 18 decimal places
    }

    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        // Getting conversion rate with 18 decimal places
        uint256 ethPrice = getPrice();
        // ethAmount and ethPrice both have 18 decimal places so need to divide by 10^18
        uint256 ethAmountInUSD = (ethPrice * ethAmount) / (10 ** 18);
        return ethAmountInUSD;
    }

    function withdraw() payable onlyOwner public {
        payable(msg.sender).transfer(address(this).balance);

        // Reseting all the funders
        for (uint256 funderIndex = 0; funderIndex < funders.length; funderIndex++){
            addressToAmountFunded[funders[funderIndex]] = 0;
            // address funder = funders[funderIndex];
            // addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
}