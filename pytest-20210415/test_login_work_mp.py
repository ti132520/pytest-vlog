# Author    ： 怕你呀
# Time      ： 2021/4/15
# File      ： test_wmp_login
# IDE       ： PyCharm
import time
from random import random, randrange
from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWmpLogin:
    # def setup_method(self, method):
    #

    def teardown_method(self, method):
        self.driver.quit()
    # 导出cookies 到yaml文件
    # def test_open_with_get_cookies(self, init_driver):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     cookies = self.driver.get_cookies()
    #     with open("user_datas/cookies.yaml", 'w') as f:
    #         yaml.dump(cookies, f)

    def test_login_work_mp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('debuggerAddress', "127.0.0.1:9222")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 导入 cookies 到网页 完成登陆
        self.driver.delete_all_cookies()
        cookies = yaml.safe_load(open('user_datas/cookies.yaml', 'r'))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

        sleep(1)
        # try:
        #     # 等待 添加成员 出现再执行
        #     WebDriverWait(self.driver, 1, 0.2).until(EC.presence_of_element_located((By.CLASS_NAME, 'js_add_member')))
        # except Exception as e:
        #     raise e

        # el = self.driver.find_element(By.LINK_TEXT, '添加成员')
        # self.driver.execute_script('arguments[0].click()', el)
        js = 'document.getElementsByClassName("qui_btn ww_btn js_add_member")[0].click()'
        self.driver.execute_script(js)
        sleep(1)
        # try:
        #     WebDriverWait(self.driver, 1, 0.2).until(EC.presence_of_element_located((By.LINK_TEXT, '保存')))
        #
        # except Exception as e:
        #     raise e
        username = 'hash'
        member = 'hash1'
        num = '18888888888'
        # + randrange(1, 9999, 4)
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(member)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(num)
        js = 'document.getElementsByClassName("qui_btn ww_btn js_btn_save")[0].click()'
        self.driver.execute_script(js)
