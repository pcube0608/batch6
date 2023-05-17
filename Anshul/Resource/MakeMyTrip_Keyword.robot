
*** Keywords ***
Navigate to MakeMyTrip.com
        open browser                https://www.makemytrip.com/                 chrome
        maximize browser window
        wait until element is visible           //a[@id="webklipper-publisher-widget-container-notification-close-div"]
        click element                           //a[@id="webklipper-publisher-widget-container-notification-close-div"]

Select one way Trip '${OneWayFrom}' to '${OneWayTo}'
    wait until element is enabled           //input[@type="text"]               5s
    click element                           //input[@type="text"]
    input text                              //input[@type="text"]               ${OneWayFrom}
    press keys                              //input[@type="text"]               ENTER
    click element                           (//input[@type="text"])[2]
    input text                              (//input[@type="text"])[2]          ${OneWayTo}
    press keys                              (//input[@type="text"])[2]          ENTER

Select Depature Date
        wait until element is enabled           //div[@aria-label="Sat May 27 2023"]                5s
        click element                           //div[@aria-label="Sat May 27 2023"]
        press keys                              //div[@aria-label="Sat May 27 2023"]                ENTER

Search Flight
        click element                           //a[text()="Search"]
