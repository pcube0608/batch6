*** Settings ***
Library         SeleniumLibrary

*** Test Cases ***
Writing test cases for google website
        Navigate to the URL
        Enter value inside the text box
*** Keywords ***
Navigate to the URL
        open browser            https://www.google.com                      Chrome
        maximize browser window

Enter value inside the text box
        input text              id:APjFqb        Waterfall model

        sleep   5
