*** Variable ***
${AllGovLinks}                  //i[@class='icon-external-link']/parent::a
${AllFormaerName}               //p[contains(@class,'MuiTypography-root MuiTypography-body1 style_memberName__Srgzp mui-style-sqip12')]


*** Keywords ***
Navigate to hpmindia.gov.in
    open browser                ${Browser_Url}                     ${Browser}
    maximize browser window


Hover to all Our Goverment links
    Mouse down on link                      //a[@href="http://presidentofindia.nic.in"]
    @{Alllist}                  get webelements                    ${AllGovLinks}
    FOR    ${List}              IN                  @{Alllist}

           click element            ${List}
           sleep                    10
           ${Text}          get text        ${List}
           IF      'Just Climate Action' == '${Text}'
                    CONTINUE
           END
    END


open the LOK SABHA Tab
          ${Handles}                                    get window handles
          switch window                                 ${Handles}[3]
          mouse down on image                           //img[@src="images/speaker.png"]
          click element                                 //p[text()="View Full Profile"]

click on former '${Former}' to print all fromer name
          wait until element is visible                 ${Former}
          click element                                 ${Former}

print all former name on cnsole
    @{FormerName}                get webelements             ${AllFormaerName}
    FOR     ${Names}       IN            @{FormerName}
            ${text_Names}    get text       ${Name}
            log to console      ${text_Names}
    END
