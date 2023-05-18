*** Settings ***
Documentation       krywords for bigbasket
Library             SeleniumLibrary
Resource            ../Configuration/UAT_bigbasket.robot
Resource            ../Configuration/QA_bigbasket.robot


*** Keywords ***
user navigate to bigbasket
    open browser    ${URL}      ${BROWSER}
    maximize browser window

user select fruit and vegetable from shop by catagory dropdown
    mouse over          ${Shop_BY_Catagory}
    sleep           3s
    click element       partial link:Fruits & Vegetables
    sleep               3s

user select price low to high
    click element       sel1
    sleep               5s
    select from list by value   sel1           string:pricelth

user change the quantity to 500gm for carrot
    mouse over      //*[text()="Carrot - Orange (Loose)"]
    sleep           6s
    click element       //*[text()='Carrot - Orange (Loose)']/../../div[2]/div/span/button
    click element       //*[text()='Carrot - Orange (Loose)']/../../div[2]/div/span/ul/li/a
    capture page screenshot

user add carrot to cart
    click element       //*[text()='Carrot - Orange (Loose)']/../../div[3]/div/div[3]/div[2]/div[2]/button
    sleep       4s
    capture page screenshot
