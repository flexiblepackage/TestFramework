*** Settings ***       
Resource    ../Utilities/LoadJson.robot
Library     ../../iOS/App/Template/Example.py
Library     ../../MISC/FilterAPI.py


*** Variables ***
${CYCLE}         1

${targetDUT}    xxx-xxx-xxx 
${router}       xxx-xxx-xxx 
${routerPW}     xxx
${delay}        1 

${Mobile}       iPhone 12
${implicit}     10

${LogName}      LogDefault
${COM}          serial-xxx 
${Pattern}      pattern    
${Search}       search

${Expect}       0       


*** Keywords ***  
Do App Test  
    [Arguments]        ${COUNT} 
    ${MobileName}      LoadJson             ${Mobile}
    &{cycle}           Create Dictionary    CYCLE    ${COUNT}       
    &{name}            Create Dictionary    NAME    ${LogName}

    ${TestExample}     Test Example              
    ...    ${MobileName}    
    ...    ${implicit}    
    ...    ${targetDUT}    
    ...    ${router}    
    ...    ${routerPW}    
    ...    ${delay}    
    ...    ${COM}    
    ...    &{name} 
    ...    &{cycle}  

    ${CompareLog}      Compare Log       
    ...    ${LogName}   
    ...    ${COM}    
    ...    ${COUNT}    
    ...    ${Pattern}   
    ...    ${Search}

    Should Be Equal    ${TestExample}    ${Expect}
    Should Be Equal    ${CompareLog}     ${Expect}  

         
*** Test Cases ***
App Test Example  
    FOR    ${COUNT}    IN RANGE    ${CYCLE} 
    Run Keyword And Continue On Failure    Do App Test        ${COUNT}         
    END
