*** Settings ***
Documentation               This is Navigate to Make My trip Website, book CHE to KOL
Library                     SeleniumLibrary
Resource                    ../Resource/MakeMyTrip_Keyword.robot

*** Variable ***
${OneWayFrom}               CHENNAI
${OneWayTo}                 KOLKATA


*** Test Cases ***
One way trip from Chennai to kolkata
    Given Navigate to MakeMyTrip.com
    When Select one way Trip '${OneWayFrom}' to '${${OneWayTo}}
    Then Select Depature Date
    And Search Flight
