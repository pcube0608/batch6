*** Settings ***
Documentation    Page elements file to store xpath for makemytrip_resource file

*** Variables ***
${switch_frame}             //iframe[@name="notification-frame-b8a69a19"]
${close1}                   //a[@class="close"]
${close2}                   //span[contains(@class, 'close_grey')]
${hotel}                    //a[contains(@href,'hotels')]
${input}                    //input[@id="city"]
${input_text}               //input[contains(@class,"autosuggest__input--open")]
${select_city}              //p[contains(text(),'${City}')]
${check_in}                 //div[@aria-label="Mon Jun 12 2023"]
${check_out}                //div[@aria-label="Sat Jun 17 2023"]
${apply_conditions}         //*[text()="Apply"]
${search}                   //button[@id="hsw_search_button"]
