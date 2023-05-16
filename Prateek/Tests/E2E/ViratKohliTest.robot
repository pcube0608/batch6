*** Settings ***
Documentation       To print atheletes from viratkohli foundation
Library             SeleniumLibrary
Library             pabot.PabotLib
Resource            ../../Resource/VKF.robot

*** Test Cases ***
Name the Atheletes of VKF
    ${valuesetname}=    Acquire Value Set
    ${browser}=     Get Value From Set   BROWSER
    log to console      ${browser}
    Given I navigate to URL       ${browser}
    When I validated page is loaded successfully
    Then I print the atheletes list
    close all browsers
