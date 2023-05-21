*** Settings ***
Library                                    SeleniumLibrary
Resource                                   ../Configuration/${ENV}_config.robot

*** Keywords ***
Navigate to prod facebook website
     open browser                              ${URL}          ${Browser}


