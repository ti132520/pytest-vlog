import time

import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class BasePage:
    __MAIN_URL = 'https://test-cdpteatl9zu1.feishu.cn/admin/index'

    def __init__(self, base_driver=None):
        if base_driver:
            self.driver = base_driver
        else:
            # 导入 cookies 到网页 完成登陆
            self.driver = webdriver.Chrome('./ui_test/chrome_driver_file/chromedriver.exe')
            self.driver.get(self.__MAIN_URL)
            self.driver.delete_all_cookies()
            with open('cookies.yaml', 'r') as f:
                cookies = yaml.load(f.read(), Loader=yaml.FullLoader)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.get(self.__MAIN_URL)
            if not self.driver.current_url == self.__MAIN_URL:
                self.driver.delete_all_cookies()
                raise Exception('登陆信息过期，请登陆后再试')
        self.driver.implicitly_wait(10)

    def find_element(self, by, ele=None):
        """
        :param by: 期望值为元组 例如：(By.ID, "id_name")
        :param ele: 默认为空，如有值，期望 by 参数一起传入 例如：By.ID, "id_name"
        :return: selenium 元素结果
        """
        if not ele:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, ele)

    def find_elements(self, by, ele=None):
        """
        :param by: 期望值为元组 例如：(By.ID, "id_name")
        :param ele: 默认为空，如有值，期望 by 参数一起传入 例如：By.ID, "id_name"
        :return: selenium 元素结果
        """
        if not ele:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, ele)

    def click_element(self, by, ele=None):
        """
        :param by: 期望值为元组 例如：(By.ID, "id_name")
        :param ele: 默认为空，如有值，期望 by 参数一起传入 例如：By.ID, "id_name"
        :return: selenium 元素结果
        """
        if not ele:
            return self.driver.find_element(*by).click()
        else:
            return self.driver.find_element(by, ele).click()

    def send_data_element(self, by, ele=None, par=None):
        """
        :param by: 期望值为元组 例如：(By.ID, "id_name")
        :param ele: 默认为空，如有值，期望 by 参数一起传入 例如：By.ID, "id_name"
        :param par: 默认为空，如有值，输入到输入框的值
        :return: selenium 元素结果
        """
        if not ele:
            return self.driver.find_element(*by).send_keys(par)
        else:
            return self.driver.find_element(by, ele).send_keys(par)

    def select_by(self, by, ele=None, cl='first', val=None):
        """
        :param by: 期望值为元组 例如：(By.ID, "id_name")
        :param ele: 默认为空，如有值，期望 by 参数一起传入 例如：By.ID, "id_name"
        :param cl: 默认为first
            select_by_index(self, index)    　　 #以index属性值来查找匹配的元素并选择；
            select_by_value(self, value)        #以value属性值来查找该option并选择；
            select_by_visible_text(self, text)  #以text文本值来查找匹配的元素并选择；
            first_selected_option(self)         #选择第一个option 选项 ；
        :param val: 默认为空 有值 则为index值 或者value值 或者text值
        :return: selenium 元素结果
        """
        if not ele:
            element = self.driver.find_element(*by)
        else:
            element = self.driver.find_element(by, ele)

        if cl == 'first':
            return Select(element).first_selected_option()
        elif cl == 'index':
            return Select(element).select_by_index(self, val)
        elif cl == 'value':
            return Select(element).select_by_value(self, val)
        elif cl == 'text':
            return Select(element).select_by_visible_text(self, val)
        else:
            return False

    def move_to_element(self, obj):
        return ActionChains(self.driver).move_to_element(obj).perform()
