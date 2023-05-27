*** Settings ***
Documentation    feature file for Guru99 website
Resource         ../Resources/Guru99_resource.robot

*** Test Cases ***
Customer login test case
    Given I navigate to website
    When I clicked on bank project
    Then I enter login credentials
