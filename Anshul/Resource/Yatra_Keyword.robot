*** Variable ***
${Depature.City}                             MUMBAI
${Arrival.City}                              GOA

*** Keywords ***
Navigate to Yatra.Com
    open browser                        https://www.yatra.com                     chrome
    maximize browser window

Accept the Cookeies
    click element           //button[text()="Ok,I Agree"]

Goto The Round Trip
    click element           //a[@title='Round Trip']

Select city '${Depature.City}' to '${Arrival.City}'
    wait until element is enabled            //input[@id='BE_flight_origin_city']           5s
    click element                            //input[@id='BE_flight_origin_city']
    input text                               //input[@id='BE_flight_origin_city']           ${DepatureCity}
    press keys                               //input[@id='BE_flight_origin_city']           ENTER
    click element                            //input[@id='BE_flight_arrival_city']
    input text                              //input[@id='BE_flight_arrival_city']           ${ArrivalCity}
    press keys                              //input[@id='BE_flight_arrival_city']           ENTER

Select goingdate and return date
    wait until element is visible       //input[@id='BE_flight_arrival_date']                5s
    click element                       //input[@id='BE_flight_arrival_date']
    click element                       //td[@id="23/06/2023"]
    wait until element is enabled       //input[@id='BE_flight_origin_date']                 5s
    click element                       //input[@id='BE_flight_origin_date']
    click element                       //td[@id="26/06/2023"]

Select The Traveller And Class
    wait until element is enabled       //i[@class="icon icon-angle-right arrowpassengerBox"]           5s
    click element                       //i[@class="icon icon-angle-right arrowpassengerBox"]
    wait untill element is visible      //span[@id="childPax"]                                          5s
    click element                       //span[text()="Economy"]
    click element                       //a[@title="Student Fare Offer"]
Search A Flight
    click element                       //input[@id="BE_flight_flsearch_btn"]



