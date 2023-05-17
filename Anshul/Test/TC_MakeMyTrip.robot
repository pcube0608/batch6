*** Settings ***
Documentation               This is Navigate



*** Test Cases ***
One way trip from Chennai to kolkata
    Given Navigate to MakeMyTrip.com
    When Select one way Trip  ${OneWay}
*** Keywords ***
Provided precondition
    Setup system under test