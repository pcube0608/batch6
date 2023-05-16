*** Settings ***
Library                 OperatingSystem
Library                 SeleniumLibrary
Resource                ../Library/CommonUtility.py

*** Keywords ***
Generate Dynamic Folder
    [Arguments]                                     ${FolderName}
    ${DynamicTimeStamp}                             generateTimeStamp
    operatingsystem.create directory                ${CURDIR}/../Results/${FolderName}/${DynamicTimeStamp}
    SeleniumLibrary.set screenshot directory        ${CURDIR}/../Results/${FolderName}/${DynamicTimeStamp}


*** Variables ***
${URL}                          http://localhost:7272
${BROWSER}                      chrome
${USERNAME}                     demo
${PASSWORD}                     bW9kZQ==
${WELCOME_URL}                  http://localhost:7272/welcome.html
${VKF Title}                    VKF Athletes – Virat  Kohli Foundation
