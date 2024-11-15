*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  liisa
    Set Password  liisa123
    Set Password Confirmation  liisa123
    Submit Registration
    Registration Should Succeed
    

Register With Too Short Username And Valid Password
    Set Username  li
    Set Password  liisa123
    Set Password Confirmation  liisa123
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 characters long


Register With Valid Username And Too Short Password
    Set Username  liisa
    Set Password  lii
    Set Password Confirmation  lii
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  liisa
    Set Password  liisaliisa
    Set Password Confirmation  liisaliisa
    Submit Registration
    Registration Should Fail With Message  Password must contain at least one special character or number

Register With Nonmatching Password And Password Confirmation
    Set Username  liisa
    Set Password  liisa123
    Set Password Confirmation  liisa1234
    Submit Registration
    Registration Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Registration Should Fail With Message  Username is already in use

*** Keywords ***
Submit Registration
    Click Button  Register

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}