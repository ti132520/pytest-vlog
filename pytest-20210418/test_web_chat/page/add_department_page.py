# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/20
# File      ： add_department_page
# IDE       ： PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from test_web_chat.page.base_page import BasePage
from test_web_chat.page.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    __name_lo = (By.XPATH, "//input[@name='name']")
    __select_party_lo = (By.CSS_SELECTOR, ".js_toggle_party_list")
    __party_find_ele_lo = (By.XPATH, "//div[@class='inputDlg_item']//a[text()='开发']")
    __ok_btn_lo = (By.XPATH, "//a[text()='确定']")

    def add_department(self, name):
        # 输入 部门名称
        self.send_data_element(self.__name_lo, par=name)
        self.click_element(self.__select_party_lo)
        self.click_element(self.__party_find_ele_lo)
        self.click_element(self.__ok_btn_lo)
        return ContactPage(self.driver)
