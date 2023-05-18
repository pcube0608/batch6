*** Settings ***
Documentation    This keyword file contains implementation of TC's for MakeMyTrip
Library         SeleniumLibrary
Resource        ../Configuration/MMTconfig_Env.robot
Resource        PageObject/MakeMyTrip_HomePage.robot

*** Keywords ***
I Navigate To MakeTrip
        open browser        ${URL}           ${Browser}
        maximize browser window

I Remove The Ads
        wait until element is visible       ${ad_frame}
        select frame    ${ad_frame}
        click element   ${Close_Btn}
        wait until element is enabled       ${Close_Btn2}
        click element   ${Close_Btn2}

I Go To Flights Section
        click element       ${Flights}

I Search for Flight
        [Arguments]    ${Depart_city}    ${Arrive_city}
        wait until element is visible   ${From}
        click element       ${From}
        wait until element is enabled       //input[@placeholder='From']
        input text          //input[@placeholder='From']         ${Depart_city}
        wait until element is enabled   ${suggest_Depart_city}
        click element       ${suggest_Depart_city}
        wait until element is visible       ${To}
        click element       ${To}
        wait until element is enabled       //input[@placeholder='To']
        input text          //input[@placeholder='To']          ${Arrive_city}
        wait until element is enabled   ${suggest_Arrive_city}
        click element       ${suggest_Arrive_city}
        click element       ${Date}
        click element       ${Search}