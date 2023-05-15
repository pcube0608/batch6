*** Settings ***
Library         SeleniumLibrary
Library         ../Library/Decode.py
Library         ../Library/CommonUtility.py
Library             OperatingSystem
Resource            ../Resource/Pages/HomePage.robot


*** Keywords ***
I navigate to Amazon.com
    [Arguments]         ${BROWSER}
    open browser        https://amazon.in       ${BROWSER}
    capture page screenshot

I select Deals from Dropdown
    select from list by value           ${XpathAllDropdown}    ${ValueAllDropdown}
    ${decoded_value}        Decode.decode       TWFyY2hAMjAyMA==
    input text      //input[@id='twotabsearchtextbox']      ${decoded_value}

    #log to console          ${CURDIR}
    ${excel_value}        CommonUtility.Read_Excel_Value        FNAME       Data2.xls
    input text      //input[@id='twotabsearchtextbox']      ${excel_value}
    capture page screenshot

Deals got selected in All Category
    log to console      Successfully selected