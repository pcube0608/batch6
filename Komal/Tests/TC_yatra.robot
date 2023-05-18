*** Settings ***
Library             SeleniumLibrary
Library      Screenshot
Documentation    Yatra plan your trip right now
Resource         ../Resource/yatra_rss.robot

*** Test Cases ***
Yatra plan your journey
        user Navigate to yatra website
        Select the trip
        Select the date
        Select the class
        Search the flight