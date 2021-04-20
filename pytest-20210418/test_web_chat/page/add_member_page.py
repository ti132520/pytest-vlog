# Author    ： 怕你呀
# Time      ： 2021/4/18
# File      ： add_member
# IDE       ： PyCharm
import time

from selenium.webdriver.common.by import By
from test_web_chat.page.base_page import BasePage
from test_web_chat.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    __username_lo = (By.ID, "username")
    __memberAdd_acctid_lo = (By.ID, "memberAdd_acctid")
    __memberAdd_phone_lo = (By.ID, "memberAdd_phone")
    __js_btn_save = (By.CSS_SELECTOR, ".js_btn_save")
    __get_failed_list_of_lo = (By.CSS_SELECTOR, ".ww_inputWithTips_tips")

    def add_member(self, username, acctid, phone):

        self.send_data_element(self.__username_lo, '', username)
        self.send_data_element(self.__memberAdd_acctid_lo, '', acctid)
        self.send_data_element(self.__memberAdd_phone_lo, '', phone)
        self.click_element(self.__js_btn_save)

        return ContactPage(self.driver)

    def add_member_failed(self, username, acctid, phone):

        self.send_data_element(self.__username_lo, '', username)
        self.send_data_element(self.__memberAdd_acctid_lo, '', acctid)
        self.send_data_element(self.__memberAdd_phone_lo, '', phone)
        self.click_element(self.__js_btn_save)
        failed_list = []
        element_list = self.find_elements(self.__get_failed_list_of_lo)
        for element in element_list:
            failed_list.append(element.text)

        return failed_list
