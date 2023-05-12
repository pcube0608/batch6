*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Writing test cases for google website
    Navigate to the url
    Enter Value inside the text box

*** Keywords ***
Navigate to the url
    open browser        https://www.google.com/     chrome
    maximize browser window

Enter Value inside the text box
    input text      id:APjFqb       Automation

    sleep       5