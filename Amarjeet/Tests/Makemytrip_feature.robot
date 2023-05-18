*** Settings ***
Documentation    Feature file for makemytrip website automation
Resource        ../Resources/Makemytrip_resource.robot


*** Variables ***
${City}          Mumbai

*** Test Cases ***
Check if the user is able to search hotels
    Given Navigate to makemytrip website
    When Select the hotel section
    Then Search for place                ${City}
