# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/16
# File      ： main_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy as By
from appium.webdriver.webdriver import WebDriver

from page.base_page import BasePage
from page.quotation_page import QuotationPage


class MainPage(BasePage):
    __by_of_quotation = (By.XPATH, '//*[@text="行情"]')

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def goto_quotation(self):
        self.click_element(self.__by_of_quotation)
        return QuotationPage(self.driver)
