// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

// this is the malicious contract (caller)
contract caller {

    // replicate event declaration of target contract
    event called(address msg_sender, address thisAddress);

    // replicate enum declaration of target contract used for testing the result of the delegatecall()
    uint public enum_test;

    // variable used to store the address of the target contract
    address public immutable callee;

    constructor(address calleeAdress) {
        callee=calleeAdress;
    }

    // do a delegatecall to call the target contract (callee)
    function test_delegate_call() external returns(bool) {

        // data used in the delegatecall
        bytes memory data_call = abi.encodeWithSignature("generateEvent()");
        // delegatecall execution, targeting the callee contract
        (bool success, bytes memory return_data) = callee.delegatecall(data_call);

        return success;
    }

}