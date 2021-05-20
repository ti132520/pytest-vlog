# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/14
# File      ： web
# IDE       ： PyCharm
import os

from selenium import webdriver

from page.base_page import BasePage
from page.main_page import MainPage

url = 'https://www.baidu.com'
browser = 'chrome'


class Web(BasePage):
    def __init__(self, driver: webdriver = None):
        self.driver = driver



    def start(self):

        browser = os.getenv("browser").lower()
        if browser == 'headless':
            self.driver = webdriver.PhantomJS()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()


        self.driver.implicitly_wait(5)
        self.driver.get(url)

    def goto_main(self):
        return MainPage(self.driver)

    def restart(self):
        self.driver.get(url)

    def stop(self):
        self.driver.quit()
