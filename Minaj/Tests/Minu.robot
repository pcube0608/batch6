*** Settings ***
Documentation    Yatra plan your trip right now
Resource         ../Resources/res_robot.robot

*** Test Cases ***
Yatra plan your journey
        Given Navigate to yatra website
        When Select the trip
        And Select the date
        And Select the class
        Then Search the flight
