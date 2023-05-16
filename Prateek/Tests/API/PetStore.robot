*** Settings ***
Library         RequestsLibrary

*** Variables ***
${AliasName}            Test
${BASE_URL}             https://petstore.swagger.io



*** Test Cases ***
Test API for Pets
    [Tags]    DEBUG
    To check if we can get pet details

*** Keywords ***
To check if we can get pet details
    create session          ${AliasName}            ${BASE_URL}
    ${response}             GET On Session          ${AliasName}        /v2/pet/100
    log to console          ${response.content}
    ${status_code}          convert to string       ${response.status_code}
    should contain          ${status_code}          200