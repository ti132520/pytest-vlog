import time

import pytest
import yaml
from selenium import webdriver


@pytest.mark.test_login
def test_login():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://test-cdpteatl9zu1.feishu.cn/admin/index')
    with open('cookies.yaml', 'r') as f:
        cookies = yaml.load(f.read(), Loader=yaml.FullLoader)
        for cookie in cookies:
            print('当前domain')
            print(cookie.get('domain'))
            driver.add_cookie(cookie)
    driver.get('https://test-cdpteatl9zu1.feishu.cn/calendar/week')
    time.sleep(10)
