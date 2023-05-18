*** Settings ***
#Documentation    Suite descriptionrobot
Library         SeleniumLibrary
*** Variable ***

${url}   https://www.google.com/
${Browser}      chrome

*** Test Cases ***
google search
     Open Browser     ${url}     ${Browser}
     Maximize Browser Window

