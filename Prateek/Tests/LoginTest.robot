*** Settings ***
Library                 SeleniumLibrary
Resource                ../../Resource/Login.robot


*** Test Cases ***
Login TestCase
    Given I navigated to Server "http://localhost:7272"
    When I Entered "demo" and Password
    And I Clicked on Submit Button
    Then I am able to login successfully        http://localhost:7272/welcome.html      676         988
    And I Verify that I am on Welcome Page

