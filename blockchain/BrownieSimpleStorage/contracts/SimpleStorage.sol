// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    // This will get initialized to 0!
    uint256 favoriteNumber;
    // bool favoriteBool = false;
    // string favoriteString = "String";
    // int256 favoriteInt = -5;
    // address favoriteAddress = 0xbB66eF34814f0613a3B738288FE55553A69C44BA;
    // bytes32 favoriteBytes = "Cat";

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    // Single person
    // People public person = People({favoriteNumber: 2, name: "Patrick"});

    // Array of people
    People[] public people; // Dynamic Array
    mapping(string => uint256) public nameToFavoriteNumber;

    // People[1] // Fixed size array

    // Define a function
    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
