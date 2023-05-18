*** Settings ***
Documentation    All The Address Of The webelement Used In Resources Of MakeMyTrip

*** Variables ***
${ad_frame}                 //iframe[@title = 'notification-frame-b8a69a19']
${Close_Btn}                //a[@class = 'close']
${Close_Btn2}               //span[contains(@class, 'close_grey')]
${Flights}                  //li[@class='menu_Flights']
${From}                     //input[@id='fromCity']
${suggest_Arrive_city}      //ul[@role='listbox']/li[1]
${suggest_Depart_city}      //ul[@role='listbox']/li//p[text()='New Delhi, India']
${To}                       //input[@id='toCity']
${Search}                   //a[text()='Search']
${Date}                     //div[@aria-label='Wed May 31 2023']