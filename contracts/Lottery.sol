// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Lottery{
    address public manager;
    address payable[] public players;

    constructor(){
        manager = msg.sender;
    }

    function getBalance() public view returns(uint){
        return address(this).balance;
    }

    function buyLottery() public payable {
        require(msg.value == 1 ether,"Please buy lottery 1 eth only");
        players.push(payable(msg.sender));
    }

    function getLength() public view returns(uint){
        return players.length;
    }

    function randomLottery() private view returns(uint){
        return uint(keccak256(abi.encodePacked(block.difficulty,block.timestamp,players.length)));
    }

    function selectWinner() public{
        require(msg.sender == manager,"You don't manager");
        require(getLength() > 2,"less then 2 lottery");
        uint pickrandom = randomLottery();
        address payable winner;
        uint selectIndex = pickrandom % players.length;
        winner = players[selectIndex];
        winner.transfer(getBalance());
        players = new address payable[](0);
    }
}