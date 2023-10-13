// SPDX-License-Identifier: MIT

pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

// import "@openzeppelin/contracts/access/Ownable.sol";

contract PaymentToken is ERC20 {
    constructor(uint256 _initialSupply) ERC20("PaymentToken", "PayTok") {
        _mint(address(this), _initialSupply);
    }
}
