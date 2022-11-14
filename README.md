## What does it do
Testframework is based on Robotframework and Python to build an environment for IoT products integration tests.

Including selenium for webs, appium for iOS and Android, and serial port API to filter embedded system debug logs.

## How do I use it
- mobile tests for example:

Build your script here at Android/App/Template and import it from the RobotExample.

![Screenshot 2022-11-13 143445](https://user-images.githubusercontent.com/98958185/201509124-12264a1c-46c9-4cae-9a4c-f5a11e437321.png)
![Screenshot 2022-11-13 143310](https://user-images.githubusercontent.com/98958185/201509077-f32ea556-e6fe-4701-9591-888bea58b330.png)

- web tests for example:

![Screenshot 2022-11-13 143617](https://user-images.githubusercontent.com/98958185/201509185-e6a0a872-68c9-4801-b33d-8d59cbbb542a.png)
![Screenshot 2022-11-13 144815](https://user-images.githubusercontent.com/98958185/201509552-62ccebad-1924-4fe8-a13b-769744c3f564.png)


## Environments
- Locally on Mac, or Windows ("RobotExample" folder for example).
- CI services: such as Jenkins, Azure DevOps ("CI Configs" folder for example).
- Serverless hosting such as Vercel (see "api" folder for example).


## CI Services
You can use variables to define which test case will be execute.

For example: 

robot --pythonpath . -d ./results/ -T -x result.xml ./Robot/TestCase/$(Robot).robot

P.S. Azure DevOps is recommended because I like it.


## Serverless hosting
You can make your test cases into web APIs, that will execute the tests and present the results when someone visits your web page.

For example:

https://test-framework-lilac.vercel.app/

Excute test case by visit "api"

https://test-framework-lilac.vercel.app/api

