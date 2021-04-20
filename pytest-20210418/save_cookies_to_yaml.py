# -*- coding: utf-8 -*-
# Author    ： 怕你呀
# Time      ： 2021/4/18
# File      ： save_cookies_to_yaml
# IDE       ： PyCharm
import os
from time import sleep

import yaml
from selenium import webdriver


def main():
    """
    运行前请先使用 " chrome --remote-debugging-port=9222 " 命令打开google 调试窗口
    :return:
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option(name='debuggerAddress', value="127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    driver.implicitly_wait(3)
    print('请在浏览器中扫码登陆企业微信')
    time = 0
    while True:
        sleep(1)
        time = time + 1
        print("\r", end=" ")
        print("{} {}".format('等待扫码：', str(time) + ' 秒'), end="")
        if driver.current_url == 'https://work.weixin.qq.com/wework_admin/frame#index':
            # 把正常状态的cookies 保存到yaml文件
            cookies = driver.get_cookies()
            f = open("test_web_chat/user_data/cookies.yaml", 'w')
            yaml.dump(cookies, f)
            f.close()
            quit('\n 登陆并保存cookies 完成')


if __name__ != 'main':
    main()
