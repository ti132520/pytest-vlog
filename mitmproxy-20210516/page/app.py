# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/16
# File      ： app
# IDE       ： PyCharm
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.main_page import MainPage


class App(BasePage):
    def __init__(self, driver: WebDriver = None):
        if driver:
            self.driver = driver
        else:
            caps = {
                "platformName": "android", "deviceName": "1", "appPackage": "com.xueqiu.android",
                "appActivity": ".common.MainActivity ",
                "noReset": True,
                "settings[waitForIdleTimeout]": 0, "skipDeviceInitialization": True, "dontStopAppOnReset": True
            }
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def start(self):
        self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
