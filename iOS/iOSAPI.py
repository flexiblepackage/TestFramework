from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECs
from selenium.common.exceptions import WebDriverException
from MISC.ExceptAPI import ExceptAPI


class iOSAPI(ExceptAPI):

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

    def InitApp(self, caps, implicit):
        self._implicit = implicit
        self._driver = webdriver.Remote(
            "http://localhost:4723/wd/hub", caps)
        self._driver.implicitly_wait(self._implicit)

    def ClickLabel(self, label):
        self._driver.find_element(
            AppiumBy.IOS_PREDICATE, 'label == "'+label+'"').click()

    def ClickName(self, name):
        self._driver.find_element(
            AppiumBy.IOS_PREDICATE, 'name == "'+name+'"').click()

    def ClickValue(self, value):
        self._driver.find_element(
            AppiumBy.IOS_PREDICATE, 'value == "'+value+'"').click()

    def ClickXpath(self, xpath):
        self._driver.find_element(
            AppiumBy.XPATH, xpath).click()

    def KeyLabel(self, label, sendText):
        self._driver.find_element(
            AppiumBy.IOS_PREDICATE, 'label == "'+label+'"').clear().send_keys(sendText)

    def KeyName(self, name, sendText):
        self._driver.find_element(
            AppiumBy.IOS_PREDICATE, 'name == "'+name+'"').clear().send_keys(sendText)

    def KeyValue(self, value, sendText):
        self._driver.find_element(
            AppiumBy.IOS_PREDICATE, 'value == "'+value+'"').clear().send_keys(sendText)

    def KeyXpath(self, xpath, sendText):
        self._driver.find_element(
            AppiumBy.XPATH, xpath).send_keys(sendText).clear().send_keys(sendText)

    @__Screen
    @ExceptAPI.Catch
    def DetectLabel(self, label, time, screenShot: bool, screenBool: bool, **kwargs):
        self._driver.implicitly_wait(time)
        self._driver.find_element(
            AppiumBy.IOS_PREDICATE, 'label == "'+label+'"')
        self._driver.implicitly_wait(self._implicit)

    def VisiableLable(self, label, time, **kwargs):
        self._driver.implicitly_wait(time)
        err = self._driver.find_element(
            AppiumBy.IOS_PREDICATE, 'label == "'+label+'"').is_displayed()
        return err

    # @__Screen
    # @Except
    # def DetectLabel2(self, xpath, time, screenShot: bool, screenBool: bool, **kwargs):
    #     self._driver.implicitly_wait(time)
    #     wait = WebDriverWait(self.driver, time)
    #     wait.until(ECs.visibility_of_element_located(AppiumBy.XPATH,xpath))
    #     self._driver.implicitly_wait(self._implicit)

    @__Screen
    @ExceptAPI.Catch
    def DetectName(self, name, time, screenShot: bool, screenBool: bool, **kwargs):
        self._driver.implicitly_wait(time)
        self._driver.find_element(AppiumBy.IOS_PREDICATE, 'name == "'+name+'"')
        self._driver.implicitly_wait(self._implicit)

    # def Swipe(self, direction):  # diretion = up | down | left | right
    #     self._driver.execute_script(
    #         "mobile: scroll", [{"direction": direction}])

    # def SwipeLabel(self, label, direction):
    #     locator = self._driver.find_element(
    #         AppiumBy.IOS_PREDICATE, 'label == "'+label+'"')
    #     self._driver.execute_script(
    #         "mobile: scroll", [{"direction": direction, "element": locator}])

    def SwipeScreen(self, direction):
        dut_size = self._driver.get_window_size()
        Yup_point = dut_size["height"]/3
        Ydown_point = dut_size["height"]/3 * 2
        Xleft_point = dut_size["width"]/3
        Xright_point = dut_size["width"]/3 * 2
        if (direction == "UP"):
            self._driver.swipe(Xleft_point, Yup_point,
                               Xleft_point, Ydown_point, 60)
        elif (direction == "DOWN"):
            self._driver.swipe(Xleft_point, Ydown_point,
                               Yup_point, Yup_point, 60)
        elif (direction == "LEFT"):
            self._driver.swipe(Xleft_point, Yup_point,
                               Xright_point, Yup_point, 40)
        elif (direction == "RIGHT"):
            self._driver.swipe(Xright_point, Ydown_point,
                               Xleft_point, Ydown_point, 40)

    def SwipeLabel(self, label, direction):
        element_locate = self._driver.find_element(
            AppiumBy.IOS_PREDICATE, 'label == "'+label+'"')
        dut_size = element_locate.size
        dut_pos = element_locate.location
        Yup_point = dut_pos["y"] + dut_size["height"]/4
        Ydown_point = dut_pos["y"] + dut_size["height"]*0.75
        Xleft_point = dut_pos["x"] + dut_size["width"]/4
        Xright_point = dut_pos["x"] + dut_size["width"]*0.75
        if (direction == "UP"):
            self._driver.swipe(Xleft_point, Yup_point,
                               Xleft_point, Ydown_point, 100)
        elif (direction == "DOWN"):
            self._driver.swipe(Xleft_point, Ydown_point,
                               Yup_point, Yup_point, 100)
        elif (direction == "LEFT"):
            self._driver.swipe(Xright_point, Ydown_point,
                               Xleft_point, Ydown_point, 100)
        elif (direction == "RIGHT"):
            self._driver.swipe(Xleft_point, Yup_point,
                               Xright_point, Yup_point, 100)

    def Quit(self):
        self._driver.reset()
        self._driver.quit()
