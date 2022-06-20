from brownie import *
from brownie.network.state import Chain
# from web3 import Web3, eth
import pytest

def main():
    
    deployer = accounts[0]

    # get the block number before start
    block_nb = network.chain.height

    # contracts deployment
    callee_contract = callee.deploy({"from": deployer, "priority_fee": 2})
    caller_contract = caller.deploy(callee_contract, {"from": deployer, "priority_fee": 2})

    # print addresses
    print('- deployer: ', deployer)
    print('- callee address: ', callee_contract)
    print('- caller address: ', caller_contract)

    # create the events container for each contract
    callee_contractEvents = network.contract.ContractEvents(callee_contract)
    caller_contractEvents = network.contract.ContractEvents(caller_contract)

    print('- enum_test before: ', callee_contract.enum_test())

    # call the function executing the delegatecall
    tx = caller_contract.test_delegate_call({"from": deployer, "priority_fee": 2})
    return_tx = tx.return_value
    tx_events = tx.events
    callee_events = callee_contractEvents.get_sequence(block_nb,None)
    caller_events = caller_contractEvents.get_sequence(block_nb,None)

    # print results of delegatecall tx
    print('*** delegatecall tx ***')
    print('- return_tx: ', return_tx)
    print('- tx events: ', tx.events)
    print('- callee events: ',callee_events)
    print('- caller events: ',caller_events)
    print('- enum_test after delegatecall: ', caller_contract.enum_test())

    # call the function directly
    tx_direct = callee_contract.generateEvent({"from": deployer, "priority_fee": 2})
    tx_direct_events = tx_direct.events
    callee_events = callee_contractEvents.get_sequence(block_nb,None)
    caller_events = caller_contractEvents.get_sequence(block_nb,None)

    # print results of direct tx
    print('*** direct tx ***')
    print('- tx_direct events: ', tx_direct_events)
    print('- callee events: ',callee_events)
    print('- caller events: ',caller_events)
    print('- enum_test after direct call: ', callee_contract.enum_test())



