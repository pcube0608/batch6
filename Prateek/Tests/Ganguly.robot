*** Settings ***
Library         SeleniumLibrary
Library         RequestsLibrary
Library         Collections
Library         OperatingSystem


*** Test Cases ***
Test title
    [Tags]    DEBUG
    I navigate to Saurav Website
    I send API

*** Keywords ***
I navigate to Saurav Website
    open browser        https://souravganguly.co.in/        chrome
    click element        css:.mobile-toggle
    wait until element is visible       //a[text()='Records & Accolades']
    click element        //a[text()='Records & Accolades']
    scroll element into view        css:#table_1
    ${count}        get element count       //td[starts-with(text(),'Runs')]/following-sibling::td
    FOR     ${index}        IN RANGE        1       ${count}+1
        ${test}         get text        //td[starts-with(text(),'Runs')]/following-sibling::td[${index}]
        log to console     ${test}
    END

I send API
    Create Session          Test        https://petstore.swagger.io
    ${resp}         Get On Session     Test        /v2/store/inventory
    log to console      ${resp.status_code}