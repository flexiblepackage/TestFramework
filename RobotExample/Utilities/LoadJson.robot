*** Settings ***
Library    OperatingSystem
Library    json


*** Keywords ***
LoadJson
    [Arguments]    ${Mobile}
    ${json}        Get File    ./Robot/MobileCaps/${Mobile}.json
    ${jsonstr}     Evaluate    json.loads('''${json}''')    json 
    RETURN         ${jsonstr} 
