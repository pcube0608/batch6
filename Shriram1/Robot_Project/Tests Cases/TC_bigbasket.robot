*** Settings ***
Documentation   test cases for bigbasket cart
Resource    ../Resource/Resource_bigbasket.robot

*** Test Cases ***
To verify if user is able to add vegetables to cart
    Given user navigate to bigbasket
    When user select fruit and vegetable from shop by catagory dropdown
    And user select price low to high
    And user change the quantity to 500gm for carrot
    Then user add carrot to cart