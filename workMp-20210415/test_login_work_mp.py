# Author    ： 怕你呀
# Time      ： 2021/4/15
# File      ： test_wmp_login
# IDE       ： PyCharm
import time
from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWmpLogin:
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('debuggerAddress', "127.0.0.1:9222")
        self.driver = webdriver.Chrome(chrome_options=options)

    def teardown_method(self, method):
        self.driver.quit()
    # 导出cookies 到yaml文件
    # def test_open_with_get_cookies(self, init_driver):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #     cookies = self.driver.get_cookies()
    #     with open("user_datas/cookies.yaml", 'w') as f:
    #         yaml.dump(cookies, f)

    def test_login_work_mp(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 导入 cookies 到网页 完成登陆
        cookies = yaml.safe_load(open('user_datas/cookies.yaml', 'r'))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        # 隐性等待
        self.driver.implicitly_wait(5)
        # 等待 添加成员 出现再执行
        WebDriverWait(self.driver, 10, 0.2).until(EC.presence_of_element_located(
            By.LINK_TEXT, "添加成员124"
        ))
        # self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        # username = hash(time.time())
        # num = '1888888' + range(0000, 9999)
        # self.driver.find_element(By.ID, "username").send_keys(username)
        # self.driver.find_element(By.ID, "memberAdd_phone").send_keys(num)
