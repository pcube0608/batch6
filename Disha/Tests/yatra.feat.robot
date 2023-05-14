*** Settings ***
Resource                ../Resources/yatra.res.robot

*** Test Cases ***
Yatra plan your journey
    Given Navigate to yatra website
    When Select the trip
    And Select the date
    And Select the class
    Then Search the flight
