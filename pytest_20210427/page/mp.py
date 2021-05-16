# -*- coding: utf-8 -*-
# Author    ： 怕你呀
# Time      ： 2021/4/28
# File      ： mp
# IDE       ： PyCharm
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.main_page import MainPage


class Mp(BasePage):
    def __init__(self, driver: WebDriver = None):
        if driver:
            self.driver = driver
        else:

            caps = {
                "platformName": "android", "deviceName": "wechat", "appPackage": "com.tencent.mm",
                "appActivity": ".ui.LauncherUI", "noReset": True,
                "settings[waitForIdleTimeout]": 0, "skipDeviceInitialization": True, "dontStopAppOnReset": True
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def start(self):
        self.driver.launch_app()
        return MainPage(self.driver)

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()
