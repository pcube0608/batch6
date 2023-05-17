*** Settings ***
Documentation    Define keywords for feature file
Library          SeleniumLibrary

*** Variables ***
${Allcategories}                    //div[@class="nav-search-scope nav-sprite"]
${ListOfAllCategories}              //select[@id="searchDropdownBox"]/option

*** Keywords ***
Navigate to Amazon.com
    open browser              https://www.amazon.com                    chrome
    maximize browser window



Goto all search categories
     click element            ${Allcategories}
     sleep                    10


Toggle all categories one by one

    @{ListOfCategories}         get webelements           ${ListOfAllCategories}

    FOR     ${Categories}       IN            @{ListOfCategories}
            ${text_categories}    get text       ${Categories}
            log to console      ${text_categories}
    END

