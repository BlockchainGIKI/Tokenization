// SPDX-License-Identifier: MIT

pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {PaymentToken} from "./PaymentToken.sol";

contract Bond is ERC20, Ownable {
    address public admin;
    uint256 public supply;
    uint256 public price;
    uint256 public fee_rate;
    uint256 public fee_days_interval;
    string public fee_type;
    uint256 public end_time;

    uint256 public init_time;
    PaymentToken private payment_token;

    uint256 public constant secondsInADay = 86400;

    struct User {
        string name;
        bool status;
    }
    mapping(address => User) public addressToUser;

    enum BOND_STATE {
        Initiated,
        Available,
        Paused,
        Cash_Out_Enabled
    }
    BOND_STATE public bond_state;

    constructor(
        uint256 _initialSupply,
        address _payment_token,
        uint256 _price,
        uint256 _fee_rate,
        uint256 _fee_days_interval,
        string memory _fee_type,
        uint256 _end_time
    ) ERC20("Bond", "BND") {
        _mint(address(this), _initialSupply);
        admin = msg.sender;
        supply = _initialSupply;
        price = _price;
        fee_rate = _fee_rate;
        fee_days_interval = _fee_days_interval;
        fee_type = _fee_type;
        bond_state = BOND_STATE.Initiated;
        end_time = _end_time;
        payment_token = PaymentToken(_payment_token);
    }

    function userExists(address _user) public view returns (bool) {
        User memory user = addressToUser[_user];
        return bytes(user.name).length > 0;
    }

    function addUser(address _user, string memory _name) public onlyOwner {
        require(!userExists(_user), "This user aleady exists!");
        addressToUser[_user].name = _name;
        addressToUser[_user].status = true;
    }

    function removeUser(address _user) public onlyOwner {
        require(userExists(_user), "This user does not exist!");
        require(addressToUser[_user].status, "This user is already deleted");
        addressToUser[_user].status = false;
    }

    function getPrice() public view returns (uint256) {
        uint256 temp_end_time = end_time;
        uint256 current_time = block.timestamp;
        if (current_time <= temp_end_time) {
            temp_end_time = current_time;
        }
        uint256 time_elasped_in_days = (temp_end_time - init_time) /
            secondsInADay;
        // string memory simple = "Simple";
        if (time_elasped_in_days == 0) {
            return price;
        } else if (
            keccak256(abi.encodePacked(fee_type)) ==
            keccak256(abi.encodePacked("Compound"))
        ) {
            return
                (price * ((price + 1000) ** time_elasped_in_days)) /
                1000 ** time_elasped_in_days;
        } else {
            return price + (price * time_elasped_in_days * fee_rate) / 1000;
        }
    }

    function start() public onlyOwner {
        require(
            bond_state == BOND_STATE.Initiated,
            "The bond contract has not been initialized yet"
        );
        bond_state = BOND_STATE.Available;
        init_time = block.timestamp; // best practice: use an oracle to get the current time
    }

    function setEnd(uint256 _end_time) public onlyOwner {
        require(
            bond_state == BOND_STATE.Available,
            "The bond duration has not started yet"
        );
        require(_end_time < end_time, "The bond duration has ended");
        end_time = _end_time;
    }

    function pause() public onlyOwner {
        require(bond_state == BOND_STATE.Available);
        bond_state = BOND_STATE.Paused;
    }

    function unpause() public onlyOwner {
        require(bond_state == BOND_STATE.Paused);
        bond_state = BOND_STATE.Available;
    }

    function buy(uint256 _amount) public {
        require(
            bond_state == BOND_STATE.Available,
            "The bond duration has not started yet"
        );
        require(
            userExists(msg.sender),
            "This user is not allowed to purchase bonds"
        );
        require(
            payment_token.balanceOf(msg.sender) > _amount * getPrice(),
            "You do not have sufficient tokens to purchase bonds"
        );
        // _mint(address(this), _amount); For some reason Cheesecake Labs increased amount of bonds evertime bonds are purchased
        uint256 total = _amount * getPrice();
        payment_token.approve(address(this), total);
        payment_token.transferFrom(msg.sender, address(this), total);
        transfer(msg.sender, total);
    }

    function withdraw(uint256 _amount) public onlyOwner {
        require(
            bond_state == BOND_STATE.Available ||
                bond_state == BOND_STATE.Paused
        );
        require(payment_token.balanceOf(address(this)) >= _amount);
        payment_token.transfer(msg.sender, _amount);
    }

    function enableCashOut() public onlyOwner {
        require(
            bond_state == BOND_STATE.Available ||
                bond_state == BOND_STATE.Paused
        );
        require(block.timestamp >= end_time);
        require(payment_token.balanceOf(address(this)) > getPrice() * supply);
        bond_state = BOND_STATE.Cash_Out_Enabled;
    }

    function cashOut() public {
        require(bond_state == BOND_STATE.Cash_Out_Enabled);
        require(userExists(msg.sender), "This user does not exist");
        uint256 total_payment = balanceOf(msg.sender) * getPrice();
        _burn(msg.sender, total_payment);
        payment_token.transfer(msg.sender, total_payment);
    }
}
