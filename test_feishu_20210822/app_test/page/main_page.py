# -*- coding: utf-8 -*-
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： main_page
# IDE       ： PyCharm
from appium.webdriver.common.mobileby import MobileBy

from app_test.page.base_page import BasePage
from app_test.page.calendar_page import CalendarPage


class MainPage(BasePage):
    __by_calendar_lo = (MobileBy.XPATH, '//*[@resource-id="com.ss.android.lark:id/tab_calendar"]')
    __by_calendar_list_lo = (MobileBy.XPATH, '//*[@resource-id="com.ss.android.lark:id/function_btn_2"]')

    def goto_calendar(self):
        self.click_element(self.__by_calendar_lo)
        self.click_element(self.__by_calendar_list_lo)

        return CalendarPage(self.driver)

