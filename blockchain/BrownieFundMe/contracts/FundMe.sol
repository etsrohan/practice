// SPDX-License-Identifier: MIT
// Note: We need to deploy this on the testnet. Here we are using the Rinkeby TestNet
// or deploy a mock.

pragma solidity >=0.6.6 <0.9.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    // Mapping of Addresses to Value
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;
    AggregatorV3Interface public priceFeed;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the Owner can withdraw the money!");
        _;
    }

    constructor(address _priceFeed) {
        owner = msg.sender;
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    // Function that can accept payment
    function fund() public payable {
        // $50 Minimum threshold
        uint256 minimumUSD = 50 * 10**18;
        // what the ETH -> USD confersion rate is
        // Use a decentralized oracle network - Chainlink
        require(
            getConversionRate(msg.value) >= minimumUSD,
            "You need to spend more ETH!"
        );
        addressToAmountFunded[msg.sender] += msg.value;
        // Add funder to funders array
        funders.push(msg.sender);
    }

    // Get version function calling version function in the interface from
    // AggregatorV3Interface.sol
    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        // Answer returns price of ETH in USD with 8 decimal places
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer * 10**10); // Getting Price of ETH in USD with 18 decimal places
    }

    function getConversionRate(uint256 ethAmount)
        public
        view
        returns (uint256)
    {
        // Getting conversion rate with 18 decimal places
        uint256 ethPrice = getPrice();
        // ethAmount and ethPrice both have 18 decimal places so need to divide by 10^18
        uint256 ethAmountInUSD = (ethPrice * ethAmount) / (10**18);
        return ethAmountInUSD;
    }

    function withdraw() public payable onlyOwner {
        payable(msg.sender).transfer(address(this).balance);

        // Reseting all the funders
        for (
            uint256 funderIndex = 0;
            funderIndex < funders.length;
            funderIndex++
        ) {
            addressToAmountFunded[funders[funderIndex]] = 0;
            // address funder = funders[funderIndex];
            // addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }

    function getEntranceFee() public view returns (uint256) {
        // minimumUSD
        uint256 minimumUSD = 50 * 10**18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;
        return (minimumUSD * precision) / price;
    }
}
