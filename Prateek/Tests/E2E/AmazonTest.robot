*** Settings ***
Library             SeleniumLibrary
Resource            ../../Resource/Amazon.robot
Resource            ../../Configuration/Env1.robot
#Library             pabot.PabotLib
Suite Setup         Generate Dynamic Folder     Screenshots

*** Test Cases ***
To Verify Amazon HomePage
#    ${valuesetname}=    Acquire Value Set
#    ${browser}=     Get Value From Set   BROWSER
#    log to console      ${browser}
    Given I navigate to Amazon.com          chrome
    When I select Deals from Dropdown
    Then Deals got selected in All Category
    close all browsers


