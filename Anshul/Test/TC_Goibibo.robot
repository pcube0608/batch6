*** Settings ***
Documentation    This is ALL about goibibo Flight Search
Library          SeleniumLibrary
Resource         ../Resource/Goibibo_Keyword.robot
*** Test Cases ***
Goibibo FligHt Search
    Given Nevigate to Goibibo.com
    And Goto Round trip
    And Enter Depature,Arival City
    When Select a Fare Type
    Then Search A Flight