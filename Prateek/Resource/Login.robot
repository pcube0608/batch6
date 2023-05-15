*** Settings ***
Library             SeleniumLibrary
Library             ../Library/Decode.py
Resource            ../Configuration/Env1.robot
Resource            ../Resource/Pages/LoginPage.robot


*** Keywords ***
I navigated to Server "${URL1}"
    open browser            ${URL1}      ${BROWSER}
    maximize browser window

I Entered "${USER}" and Password
    input text              ${UserNameID}       ${USER}
    ${PASSWORD_DECODED}     Decode.decode       ${PASSWORD}
    input password          ${PasswordID}       ${PASSWORD_DECODED}

I Clicked on Submit Button
    click button            ${SubmitButtonID}

I am able to login successfully
    [Arguments]     ${URL2}
    location should be      ${WELCOME_URL}

I Verify that I am on Welcome Page
    title should be         Welcome Page

I navigated to URL
    [Arguments]     ${UURL}
    open browser      ${UURL}       chrome


Print all Atheletes names
    ${count}    get element count       //div[@class='box-info']/h4/a
    #${tewrw}    get text        //div[@class='box-info']/h4/a

    FOR     ${index}        IN RANGE        1       ${count}
            ${tewrw}    get text        (//div[@class='box-info']/h4/a)[${index}]
            log to console      ${tewrw}
    END

    aler

