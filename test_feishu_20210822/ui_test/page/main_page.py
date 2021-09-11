# Author    ： 怕你呀
# Time      ： 2021/4/18
# File      ： main_page
# IDE       ： PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from ui_test.page.base_page import BasePage
from ui_test.page.calendar_page import CalendarPage


class MainPage(BasePage):
    __CALENDAR_URL = 'https://test-cdpteatl9zu1.feishu.cn/calendar'

    def quit(self):
        self.driver.quit()

    def goto_calendar(self):
        self.driver.get(self.__CALENDAR_URL)
        return CalendarPage(self.driver)


