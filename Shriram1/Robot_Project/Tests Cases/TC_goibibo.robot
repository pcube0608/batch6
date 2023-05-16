*** Setting ***
Documentation       File Test cases of goibigo
Resource                ../Resources/Resource_goibibo.robot

*** Test Cases ***
Validate flight search
    navigate to goibigo website
    When User click on flights
    And User search for mumbai to delhi
    And User select journy date
    And User click on search button
    Then User should verify flights from mumbai to delhi
















