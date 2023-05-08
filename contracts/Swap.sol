// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

import "./Token.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Swap {
    IERC20 token;
    constructor(uint256 initialSupply) {
        token = new Token(initialSupply);
    }
    function getTokenAddress() public view returns(address) {
        return address(token);
    }
    function fundMe(uint256 amount) public {
        token.transferFrom(msg.sender, address(this), amount);
    }
    function withdrawMe(uint256 amount) public {
        token.transfer(msg.sender, amount);
    }
}