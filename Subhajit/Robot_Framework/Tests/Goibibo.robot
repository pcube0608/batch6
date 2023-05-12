*** Settings ***
Documentation       This Test Suite file contains all TC;s related to Goibibo
Resource            ../Resources/Goibibo_Keywords.robot

*** Test Cases ***
Validate Flight Search
    Given User nevigate to Goibibo website
    Then User click on Flight Tab
    And User search flight from Mumbai to Delhi
    And User click on Search button