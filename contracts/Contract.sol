// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "../interfaces/ISwap.sol";

contract Contract {
    function withdraw(uint256 amount, address reciever, address token) public {
        IERC20(token).transfer(reciever, amount);
    }
    function getFunds(uint256 amount, address funder) public {
        ISwap(funder).withdrawMe(amount);
    }
    function donate(uint256 amount, address reciever) public {
        ISwap(reciever).fundMe(amount);
    }
    function approve(uint256 amount, address reciever, address token) public {
        IERC20(token).approve(reciever, amount);
    }
}