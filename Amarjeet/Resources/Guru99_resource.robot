*** Settings ***
Documentation    Resource file for Guru99 website
Library          SeleniumLibrary
Resource         ../Configuration/Guru99_config.robot
Resource          PageElements/Guru99_pageelements.robot
Library          ../Library/Customer_library.py


*** Keywords ***
I navigate to website
    open browser         ${URL}                    ${Browser}
    maximize browser window

I clicked on bank project
    wait until element is enabled           ${Bank_project}
    click element                           ${Bank_project}

    ${staus_of_frame}       run keyword and return status   element should be visible   ${switch_frame}

    IF  ${staus_of_frame}== True
          select frame                            //iframe[contains(@id,'google_ads')]
          select frame                            ad_iframe
          click element                           dismiss-button
          unselect frame
    END

I enter login credentials
    wait until element is visible           ${username}
    input text             ${username}             mngr504610
    Sleep                  5s
    ${password}            decode passcode         ${password}
    input text             password                ${password}
