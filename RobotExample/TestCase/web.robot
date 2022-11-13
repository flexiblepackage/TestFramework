*** Settings ***       
Library    ../../Web/Example.py  


*** Variables ***
${CYCLE}    1

${url}      https://github.com/flexiblepackage/TestFramework           
${Expect}   0       


*** Keywords ***  
Do Web Test  
    [Arguments]        ${COUNT}     
    ${TestExample}     Test Example              
    ...    ${url}    
 

    Should Be Equal    ${TestExample}    ${Expect}


*** Test Cases ***
Web Process  
    FOR    ${COUNT}    IN RANGE    ${CYCLE} 
    Run Keyword And Continue On Failure    Do Web Test        ${COUNT}         
    END