# Author    ： 怕你呀
# Time      ： 2021/4/18
# File      ： main_page
# IDE       ： PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from test_web_chat.page.add_department_page import AddDepartmentPage
from test_web_chat.page.add_member_page import AddMemberPage
from test_web_chat.page.base_page import BasePage
from test_web_chat.page.contact_page import ContactPage


class MainPage(BasePage):
    __by_add_member_lo = (By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)')
    __by_contact_lo = (By.XPATH, '//*[@id="menu_contacts"]')
    __by_add_department1_lo = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    __by_add_department2_lo = (By.CSS_SELECTOR, ".js_create_party")

    def quit(self):
        self.driver.quit()

    def goto_main1(self):
        self.goto_main()
        return MainPage(self.driver)

    # 跳转到通讯录页面
    def goto_contact(self):
        self.click_element(self.__by_contact_lo)
        return ContactPage(self.driver)

    # 点击 添加成员 按钮
    def goto_add_member(self):
        self.click_element(self.__by_add_member_lo)
        return AddMemberPage(self.driver)

    # 跳到添加部门
    def goto_add_department_page(self):
        self.click_element(self.__by_contact_lo)
        self.click_element(self.__by_add_department1_lo)
        self.click_element(self.__by_add_department2_lo)
        sleep(10)
        return AddDepartmentPage(self.driver)


