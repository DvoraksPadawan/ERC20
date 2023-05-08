// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token is ERC20 {
    constructor(uint256 initialSupply) ERC20("Random Token", "RANDOM") {
        //uint256 initialSupply = 10 * 10 ** 18;
        _mint(msg.sender, initialSupply);
    }
}