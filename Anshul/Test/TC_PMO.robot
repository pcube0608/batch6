*** Settings ***
Documentation    This Is a PMO Assignment  in which Print Former Speaker Name
Library          SeleniumLibrary
Resource         ../Resource/PMO_Keyword.robot
Resource         ../Configuration/env_PMO.robot

*** Variable ***
${Former}                   //button[contains(text(),'Former')]

*** Test Cases ***
Print All Former Speaker Name
    Given Navigate to hpmindia.gov.in
    When Hover to all Our Goverment links
    And click on former '${Former}' to print all fromer name
    Then open the LOK SABHA Tab
    And print all former name on cnsole
