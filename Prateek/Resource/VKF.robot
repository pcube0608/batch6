*** Settings ***
Library         SeleniumLibrary
Library         ../Library/Decode.py
Library         ../Library/CommonUtility.py

Resource        ../Resource/Pages/VKFAtheletePage.robot
Resource        ../Configuration/Env1.robot

*** Keywords ***
I navigate to URL
    [Arguments]     ${BROWSER}
    open browser    https://viratkohli.foundation/vkf-athletes/      ${BROWSER}
    maximize browser window

I validated page is loaded successfully
    title should be     ${VKF Title}

I print the atheletes list
    ${count}        get element count       ${AtheleteNameXpath}
    FOR     ${index}        IN RANGE    1       ${count}
            ${AtheleteName}     get text        (//div[@class='box-info']/h4/a)[${index}]
            log to console      ${AtheleteName}
    END


