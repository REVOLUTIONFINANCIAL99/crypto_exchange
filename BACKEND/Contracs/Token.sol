// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Exchange {
    address public owner;

    // Eventos para seguimiento
    event Deposit(address indexed user, uint256 amount);
    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);

    mapping(address => uint256) private balances;

    constructor() {
        owner = msg.sender;
    }

    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero.");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    function transfer(address to, uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        require(to != address(0), "Invalid recipient address.");

        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
    }

    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance.");

        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        emit Withdraw(msg.sender, amount);
    }

    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
