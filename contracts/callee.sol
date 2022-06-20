// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

// this is the target contract (Callee)
contract callee {

    // event declaration
    event called(address msg_sender, address thisAddress);

    // variable used to test that the delegatecall actually worked
    uint public enum_test;

    function generateEvent() external {

        emit called(msg.sender, address(this));
        enum_test=2;

    }

}