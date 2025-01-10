// filepath: /crypto_exchange/contracts/Token.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token is ERC20 {
    constructor(uint256 initialSupply) ERC20("CryptoExchangeToken", "CET") {
        _mint(msg.sender, initialSupply);
    }
}