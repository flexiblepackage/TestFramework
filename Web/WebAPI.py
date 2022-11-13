from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
import re
from MISC.ExceptAPI import ExceptAPI


class WebAPI(ExceptAPI):

    def __Screen(func):
        def warp(self, text, time, screenShot: bool, screenBool: bool, **kwargs):

            err = func(self, text, time, screenShot, screenBool, **kwargs)
            text = re.sub("\\W+", "_", text)

            if "CYCLE" in list(kwargs.keys()):
                cycle = str(kwargs["CYCLE"])
            else:
                cycle = "0"

            if screenShot and screenBool and err == "0":
                self._chrome.get_screenshot_as_file(
                    "./logs/"
                    + " ndetect "
                    + text
                    + " "
                    + " CYCLE" + cycle
                    + ".png"
                )

            elif screenShot and not screenBool and err != "0":
                self._chrome.get_screenshot_as_file(
                    "./logs/"
                    + " ndetect "
                    + text
                    + " "
                    + " CYCLE" + cycle
                    + ".png"
                )
            return err
        return warp
    

    @ExceptAPI.Catch
    def Init(self, url, implicit=30, **kwargs):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        self._chrome = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=options)
        self._chrome.implicitly_wait(implicit)
        self._chrome.set_page_load_timeout(implicit)
        self._chrome.get(url)
        

    def ClickXpath(self, xpath):
        self._chrome.find_element(By.XPATH,  xpath).click()
        

    def KeyXpath(self, xpath, key):
        self._chrome.find_element(By.XPATH,  xpath).send_keys(key)
        

    @__Screen
    @ExceptAPI.Catch
    def XpathText(self, xpath, time, screenShot: bool, screenBool: bool, **kwargs):
        self._chrome.implicitly_wait(time)
        get = self._chrome.find_element(By.XPATH,  xpath).text
        return get

    @__Screen
    @ExceptAPI.Catch
    def DisplayXpath(self, xpath, time, screenShot: bool, screenBool: bool, **kwargs):
        self._chrome.implicitly_wait(time)
        err = self._chrome.find_element(By.XPATH,  xpath).is_displayed()
        return err

    @__Screen
    @ExceptAPI.Catch
    def DetectXpath(self, xpath, time, screenShot: bool, screenBool: bool, **kwargs):
        self._chrome.implicitly_wait(time)
        self._chrome.find_element(By.XPATH,  xpath)
        return str(0)

    def Quit(self, **kwargs):
        self._chrome.quit()
