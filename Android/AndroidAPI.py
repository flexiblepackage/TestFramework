from datetime import datetime
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECs
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.extensions.android.nativekey import AndroidKey
from MISC.ExceptAPI import ExceptAPI


class AndroidAPI(ExceptAPI):

    def __Offset(func):
        def wrap(self, *args, **kwargs):
            if "x" in list(kwargs.keys()) and "y" in list(kwargs.keys()):
                self._xy = [kwargs["x"], kwargs["y"]]
            else:
                self._xy = self._offset
            func(self, *args, **kwargs)
        return wrap

    def __Screen(func):
        def warp(self, text, time, screenShot: bool, screenBool: bool, **kwargs):

            err = func(self, text, time, screenShot, screenBool, **kwargs)

            if "CYCLE" in list(kwargs.keys()):
                cycle = str(kwargs["CYCLE"])
            else:
                cycle = "0"

            if screenShot and screenBool and err == "0":
                self._driver.get_screenshot_as_file(
                    "./logs/"
                    + " detect "
                    + text
                    + " "
                    + " CYCLE" + cycle
                    + ".png"
                )
            elif screenShot and not screenBool and err == "-1":
                self._driver.get_screenshot_as_file(
                    "./logs/"
                    + " ndetect "
                    + text
                    + " "
                    + " CYCLE" + cycle
                    + ".png"
                )
            return err
        return warp

    def InitApp(self, caps, implicit, **kwargs):
        if "x" in list(kwargs.keys()) and "y" in list(kwargs.keys()):
            self._offset = [kwargs["x"], kwargs["y"]]
        else:
            self._offset = [0, 0]

        self._driver = webdriver.Remote(
            "http://localhost:4723/wd/hub", caps)

        self._implicit = implicit
        self._driver.close_app()
        self._driver.implicitly_wait(self._implicit)
        self._driver.launch_app()
        self._driver.implicitly_wait(self._implicit)

    @__Offset
    def ClickResrc(self, resrcId, **kwargs):
        e = self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("' + resrcId + '")',
        )
        ActionChains(self._driver).move_to_element_with_offset(
            e, self._xy[0], self._xy[1]
        ).click().perform()

    @__Offset
    def ClickAcces(self, accessId, **kwargs):
        e = self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("' + accessId + '")',
        )
        ActionChains(self._driver).move_to_element_with_offset(
            e, self._xy[0], self._xy[1]
        ).click().perform()

    @__Offset
    def ClickText(self, text, **kwargs):
        e = self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("' + text + '")',
        )
        ActionChains(self._driver).move_to_element_with_offset(
            e, self._xy[0], self._xy[1]
        ).click().perform()

    @__Offset
    def ClickXpath(self, xpath):
        self._driver.find_element(
            AppiumBy.XPATH, xpath).click()
        
    @__Screen
    @ExceptAPI.Catch
    def ScrolltoText(self,text,time, screenShot: bool, screenBool: bool,  **kwargs):
        self._driver.implicitly_wait(time)
        e = self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
             'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("'+text+'"))',
             )
        ActionChains(self._driver).move_to_element_with_offset(
            e, self._xy[0], self._xy[1]
        ).click().perform()
        self._driver.implicitly_wait(self._implicit)

    def DetectResrc(self, resrcId, time, screenShot: bool, screenBool: bool,  **kwargs):
        self._driver.implicitly_wait(time)
        self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("' + resrcId + '")',
        )
        self._driver.implicitly_wait(self._implicit)
        

    @__Offset
    def LongtapText(self, text, **kwargs):
        e = self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("' + text + '")',
        )
        ActionChains(self._driver).move_to_element_with_offset(
            e, self._xy[0], self._xy[1]
        ).click_and_hold().pause(1).release().perform()
        
    def KeyResrc(self, resrcId, sendText):
        self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("' + resrcId + '")',
        ).clear().send_keys(sendText)

    def KeyAcces(self, accessId, sendText):
        self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("' + accessId + '")',
        ).clear().send_keys(sendText)

    def KeyText(self, text, sendText):
        self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("' + text + '")',
        ).clear().send_keys(sendText)

    @__Screen
    @ExceptAPI.Catch
    def DetectText(self, text, time, screenShot: bool, screenBool: bool,  **kwargs):
        self._driver.implicitly_wait(time)
        self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("' + text + '")',
        )
        self._driver.implicitly_wait(self._implicit)

    @__Screen
    @ExceptAPI.Catch
    def DetectResrc(self, resrcId, time, screenShot: bool, screenBool: bool,  **kwargs):
        self._driver.implicitly_wait(time)
        self._driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("' + resrcId + '")',
        )
        self._driver.implicitly_wait(self._implicit)
        
    def Enter(self):
        self._driver.press_keycode(AndroidKey.ENTER)

    def Tab(self):
        self._driver.press_keycode(AndroidKey.TAB)

    def Quit(self):
        self._driver.quit()
