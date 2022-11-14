*** Settings ***       
Library    ../../Web/Example.py  


*** Variables ***
${CYCLE}    1

${url}         https://github.com/flexiblepackage/TestFramework    
${implicit}    10               
${Expect}      0       


*** Keywords ***  
Do Web Test  
    [Arguments]        ${COUNT}     
    ${TestExample}     Test Example              
    ...    ${url}
    ...    ${implicit}  

    Should Be Equal    ${TestExample}    ${Expect}


*** Test Cases ***
Web Test Example  
    FOR    ${COUNT}    IN RANGE    ${CYCLE} 
    Run Keyword And Continue On Failure    Do Web Test        ${COUNT}         
    END
