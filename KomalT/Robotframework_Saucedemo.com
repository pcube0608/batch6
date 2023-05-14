*** Settings ***
Library      SeleniumLibrary
Library      Screenshot


*** Variables ***
${URL}                      https://www.saucedemo.com/
${User}                     standard_user
${Password}                   secret_sauce
${First_Name}                  Komal
${Last_Name}                   Kapde
${Zip}                         431112

*** Keywords ***
I Login To Sauce demo website
            open browser           ${URL}                  Chrome
            maximize browser window
            capture page screenshot

I Enter login details
            input text             //input[@placeholder='Username']            ${User}
            input text             //input[@placeholder='Password']            ${Password}
            click element                           //input[@id="login-button"]

I ADD product To Cart

            click element                          //div[@class="inventory_item"]//button[text()="Add to cart"]

            sleep                            5sec
            click element                         //a[@class="shopping_cart_link"]/span[text()="1"]
            click button                          //button[@id="checkout"]
I Fill Out Checkout Details
              input text                            //input[@placeholder='First Name']      Komal
              input text                            //input[@placeholder='Last Name']       kapde

              input text                             //input[@id="postal-code"]             431112

             click button                                    //input[@id='continue']
             click button                                    //button[@id='finish']
             capture page screenshot
             click button                                //button[@id='back-to-products']
I proceed to Logout
             click button                                    //button[@id='react-burger-menu-btn']
             click element                                   //a[contains(@id,'logout')]

*** Test Cases ***
I login Sauce Demo Test
                I Login To Sauce Demo website
                I Enter login details
                I ADD product To Cart
                I Fill Out Checkout Details
                I proceed to Logout

