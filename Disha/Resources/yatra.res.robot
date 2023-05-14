*** Settings ***
Library                                    SeleniumLibrary
Resource                                   ../Configuration/yatra_config.robot

*** Keywords ***
Navigate to yatra website
     open browser                              ${URL}          ${Browser}
     maximize browser window
     click button                              //button[text()="Ok,I Agree"]

Select the trip
    wait until element is visible      //a[@title="Round Trip"]                timeout=10s
    click element                      //a[@title="Round Trip"]
    click element                      //input[@id='BE_flight_origin_city']
    input text                         //input[@id='BE_flight_origin_city']    ${Deparature_city}
    press keys                         //input[@id='BE_flight_origin_city']    ENTER
    click element                      //input[@id='BE_flight_arrival_city']
    input text                         //input[@id='BE_flight_arrival_city']   ${Arrival_city}
    press keys                         //input[@id='BE_flight_origin_city']     ENTER
    press keys                         //input[@id='BE_flight_origin_city']     RETURN
    press keys                         //input[@id='BE_flight_arrival_city']    RETURN

Select the date
    click element                      //input[@id="BE_flight_origin_date"]
    wait until element is enabled      ${Deparature_date}
    click element                      ${Deparature_date}
    click element                      //input[@id="BE_flight_arrival_date"]
    wait until element is enabled      ${Return_date}
    click element                      ${Return_date}

Select the class
    click element                      //label[contains(text(),"Traveller(s), Class")]
    click element                      //span[@class="ddSpinnerPlus"]
    click element                      //span[text()='Business']
    sleep                              3s

Search the flight
    wait until element is visible       //input[@type="submit" and @value="Search Flights"]      timeout=5s
    scroll element into view            //input[@type="submit" and @value="Search Flights"]
    click element                       //input[@type="submit" and @value="Search Flights"]
