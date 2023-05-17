*** Keywords ***
Nevigate to Goibibo.com
    open browser            https://www.goibibo.com             chrome
    sleep                   3
    click element           xpath://span[@class="logSprite icClose"]

Goto Round trip
    click element           xpath://span[@class="sc-12foipm-82 gKWNCi"]

Enter Depature,Arival City
    click element           xpath://p[text()="Enter city or airport"]
    input text              xpath://input[@type='text']                         DELHI
    press keys              xpath://input[@type='text']                         ENTER
    sleep                   3
    input text              xpath://input[@type='text']                         PUNE
    press keys              xpath://input[@type='text']                         ENTER
    sleep                   3
    click element           xpath://span[@class="fswTrvl__done"]

Select a Fare Type
    click element           xpath://span[text()="senior citizen"]
    click element           xpath://a[@class="sc-12foipm-76 fvsOuM"]

Search A Flight
    click element           xpath://span[text()="SEARCH FLIGHTS"]

