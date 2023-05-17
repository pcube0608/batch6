*** Settings ***
Documentation       This is a Amazon File in Which Toggle through All categories
Resource            ../Resource/Amazon_Keyword.robot

*** Test Cases ***
Toggle All Categories
    Given Navigate to Amazon.com
    When Goto all search categories
    Then Toggle all categories one by one

