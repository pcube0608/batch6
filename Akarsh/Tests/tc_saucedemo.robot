*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}              https://www.saucedemo.com/
${user}                 standard_user
${password}             secret_sauce
${fn}                   Andrew
${ln}                   Baker
${zip}                  90210

*** Keywords ***
I Navigate To Saucedemo Website
    open browser        ${url}      chrome
    maximize browser window
I Enter The Login Details
    input text          //input[@placeholder = 'Username']          ${user}
    input text          //input[@placeholder = 'Password']          ${password}
    capture page screenshot
    click button        //input[@id='login-button']
I Add Product To Cart
     click button               (//div[@class='inventory_list']//button)[1]
     sleep                      5s
     click element               //a[@class='shopping_cart_link']
     click button               //button[@id='checkout']
I Fill Out Check Out Details
     input text                 //input[@placeholder = 'First Name']               ${fn}
     input text                 //input[@placeholder = 'Last Name']                ${ln}
     input text                 //input[@placeholder = 'Zip/Postal Code']          ${zip}
     capture page screenshot
     click button               //input[@id='continue']
     click button               //button[@id='finish']
     capture page screenshot
     click button               //button[@id='back-to-products']
I Proceed to Logout
     click button                 //button[@id='react-burger-menu-btn']
     click element                   //a[contains(@id,'logout')]
     capture page screenshot

*** Test Cases ***
Sauce Demo Test
    Given I Navigate To Saucedemo Website
    Then I Enter The Login Details
    Then I Add Product To Cart
    Then I Fill Out Check Out Details
    And I Proceed to Logout
