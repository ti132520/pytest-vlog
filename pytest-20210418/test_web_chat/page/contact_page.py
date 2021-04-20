# Author    ： 怕你呀
# Time      ： 2021/4/18
# File      ： contact
# IDE       ： PyCharm
import time

from selenium.webdriver.common.by import By

from test_web_chat.page.base_page import BasePage


class ContactPage(BasePage):
    __get_member_list_of_loc = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
    __get_department_list_of_loc = (By.CSS_SELECTOR, ".jstree-anchor")

    # 获取成员列表
    def get_member_list(self):
        member_list = []
        element_list = self.find_elements(self.__get_member_list_of_loc)
        for element in element_list:
            member_list.append(element.text)

        return member_list

    # 获取部门列表
    def get_department_list(self):
        element_list = self.find_elements(self.__get_department_list_of_loc)
        department_list = [element.text for element in element_list]
        return department_list
