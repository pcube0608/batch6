*** Settings ***
Documentation    Define keywords for feature file
Library          SeleniumLibrary
Resource         ../Resources/PageElements/Amazon_pageelement.robot
Resource         ../Configuration/Amazon_config.robot


*** Keywords ***
Navigate to amazon website
    open browser            ${URL}             ${Browser}
    maximize browser window

Toggle through all categories
    ${listof_categories}        get webelements             ${element}
    FOR     ${Category}       IN        ${listof_categories}
            ${text_category}    get text       ${Category}
            log to console      ${text_category}
    END

