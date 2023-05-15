*** Settings ***
Library     SeleniumLibrary

*** Variables ***


*** Keywords ***
I navigate to Saucedemo.com
    open browser         https://www.saucedemo.com/          chrome
    maximize browser window

user login with user ID
    input text       id:user-name    standard_user
    input text       id:password     secret_sauce
    click element    id:login-button

Add first product to cart
    click element   id:add-to-cart-sauce-labs-backpack
    click element   id:shopping_cart_container

go to cart
    click element   id:checkout
    input text      id:first-name       Subhajit
    input text      id:last-name        Das
    input text      id:postal-code      411057
    click element   id:continue
    click element   id:finish
    sleep   1
    get title

Log out from the current user
    click element   id:react-burger-menu-btn
    sleep   2
    click element   id:logout_sidebar_link
    close browser



*** Test Cases ***
writing test cases for SauceDemo website
    given I navigate to Saucedemo.com
    and user login with user ID
    then add first product to cart
    then go to cart
    then Log out from the current user


