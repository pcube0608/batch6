*** Settings ***
Documentation    Resource file containing keywords for makemytrip_feature file
Library          SeleniumLibrary
Resource         ../Resources/PageElements/Makemytrip_pageelement.robot
Resource         ../Configuration/Makemytrip_${ENV}_config.robot


*** Keywords ***
Navigate to makemytrip website
    open browser                        ${URL}                  ${Browser}
    maximize browser window
    wait until element is visible       ${switch_frame}         timeout=10s
    select frame                        ${switch_frame}
    click element                       ${close1}
    wait until element is enabled       ${close2}               timeout=10s
    click element                       ${close2}

Select the hotel section
    click element                       ${hotel}

Search for place
    [Arguments]                         ${City}
    sleep                               5s
    click element                       ${input}
    wait until element is enabled       ${input_text}         timeout=10s
    input text                          ${input_text}           ${City}
    wait until element is enabled       ${select_city}        timeout=10s
    click element                       ${select_city}
    sleep                               2s
    click element                       ${check_in}
    sleep                               2s
    click element                       ${check_out}
    sleep                               2s
    click element                       ${apply_conditions}
    sleep                               2s
    click element                       ${search}
    sleep                               10s
