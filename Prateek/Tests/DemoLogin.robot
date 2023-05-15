*** Settings ***
Library             SeleniumLibrary
Library             ../../Library/Decode.py

*** Test Cases ***
Testing Login
    open browser    http://localhost:7272      chrome
    maximize browser window
    input text      username_field              demo
    ${password}     Decode.decode               bW9kZQ==
    input password  password_field              ${password}
    click button    login_button
    title should be Welcome Page
    location should be  http://localhost:7272/welcome.html

*** Keywords ***
