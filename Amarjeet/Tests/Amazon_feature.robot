*** Settings ***
Documentation    Amazon toggling through categories
Resource         ../Resources/Amazon_resource.robot

*** Test Cases ***
Amazon website assignment
    Given Navigate to amazon website
    When Toggle through all categories
