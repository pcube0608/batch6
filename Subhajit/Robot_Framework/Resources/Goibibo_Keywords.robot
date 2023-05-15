*** Settings ***
Library     SeleniumLibrary

*** Keywords ***
User nevigate to Goibibo website
    open browser    https://www.goibibo.com/        chrome
    maximize browser window
    click element   xpath://span[@class='logSprite icClose']

User click on Flight Tab
    click element       xpath://a[@class='nav-link active']

And User search flight from Mumbai to Delhi
    click element    xpath://span[text()='From']//following-sibling::p
    input text       xpath://input[@type='text']       Mumbai
    press keys       xpath://input[@type='text']       ENTER
    sleep           1
    input text      xpath://input[@type='text']         Delhi
    press keys      xpath://input[@type='text']         ENTER
    click element       xpath://span[@class='fswTrvl__done']
    sleep           1
    click element       xpath://a[text()='Done']

And User click on Search button
    click element       xpath://span[contains(@class,'sc-12foipm-91')]
