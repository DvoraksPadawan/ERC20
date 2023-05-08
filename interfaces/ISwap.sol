// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

interface ISwap {
    function withdrawMe(uint256) external;
    function fundMe(uint256) external;
}