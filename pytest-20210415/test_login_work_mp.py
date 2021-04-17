# Author    ： 怕你呀
# Time      ： 2021/4/15
# File      ： test_wmp_login
# IDE       ： PyCharm
import time
from random import random, randrange
from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWmpLogin:
    def setup_method(self, method):
        # 连接debugger chrome 浏览器
        options = webdriver.ChromeOptions()
        options.add_experimental_option('debuggerAddress', "127.0.0.1:9222")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(3)
        # self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_work_mp(self):
        # 打开企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        if self.driver.current_url == "https://work.weixin.qq.com/wework_admin/frame#index":
            cookies = self.driver.get_cookies()
            r_steam = open('user_datas/cookies.yaml', 'r')
            with open("user_datas/cookies.yaml", 'w') as f:
                if yaml.safe_load(r_steam) != cookies:
                    yaml.dump(cookies, f)
                f.close()
        else:
            # 导入 cookies 到网页 完成登陆
            self.driver.delete_all_cookies()
            r_steam = open('user_datas/cookies.yaml', 'r')
            cookies = yaml.safe_load(r_steam)
            r_steam.close()
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
            if self.driver.current_url != "https://work.weixin.qq.com/wework_admin/frame#index":
                print("登陆信息过期，请登陆后再试")
            assert False
        # 点击通讯录
        self.driver.find_element(By.XPATH, "//a[@id='menu_contacts']").click()
        try:
            # 等待 添加成员 出现再执行
            WebDriverWait(self.driver, 2, 0.2).until(EC.presence_of_element_located((By.XPATH, '//a[@class="qui_btn ww_btn js_add_member"]')))
            # 睡眠2秒等待页面 js 功能 加载完成
            sleep(2)
            # 点击 添加成员 js版本
            js_add_member = 'document.getElementsByClassName("qui_btn ww_btn js_add_member")[0].click()'
            self.driver.execute_script(js_add_member)
        except Exception as e:
            raise e
        try:
            WebDriverWait(self.driver, 2, 0.2).until(EC.presence_of_element_located((By.XPATH, '//a[@class="qui_btn ww_btn js_btn_save"]')))
        except Exception as e:
            raise e
        username = 'hash'
        member = 'hash1'
        num = '18888888888'
        # + randrange(1, 9999, 4)
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(member)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(num)
        js_save = 'document.getElementsByClassName("qui_btn ww_btn js_btn_save")[0].click()'
        self.driver.execute_script(js_save)
