*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${URL}      http://robotframework.org/

*** Test Cases ***
Hello Robot
    Open Browser    ${URL}
    Sleep  5 seconds
    [Teardown]    Close Browser
