*** Settings ***
Documentation    This Is a Yatra.com Site in which book round trip
Library          SeleniumLibrary
Resource         ../Resource/Yatra_Keyword.robot


*** Variable ***
${Depature.City}                             MUMBAI
${Arrival.City}                              GOA


*** Test Cases ***
Round Trip Flight Search
    Given Navigate to Yatra.Com
    And Accept the Cookeies
    When Goto The Round Trip
    Then Select city '${Depature.City}' to '${Arrival.City}'
    And Select goingdate and return date
    And Select The Traveller And Class
    And Search A Flight


