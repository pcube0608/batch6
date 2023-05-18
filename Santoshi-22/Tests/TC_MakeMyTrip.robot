*** Settings ***
Documentation    This Tests file contains all TC's Related To MakeMyTrip
Resource         ../Resources/MakeMyTrip_Keywords.robot

*** Variables ***
${Depart_city}      New Delhi
${Arrive_city}      Mumbai

*** Test Cases ***
User Search For Flights
    Given I Navigate To MakeTrip
    Then I Remove The Ads
    Then I Go To Flights Section
    And I Search for Flight     ${Depart_city}      ${Arrive_city}

#    And I Search for Flight from "${depart.city}" to  "${arrive.city}"