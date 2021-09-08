"""
运行程序，主要是为了cookies复用
"""
import os
import yaml
from selenium import webdriver


def main():
    while True:
        os.system('cls')
        # os.system('clear')
        print('选择运行：\n 1.登录飞书并保存cookies \n 2.运行测试用例 \n 3.退出程序')
        select = str(input('输入选择：'))
        print(select)
        if select == '1':
            save_cookies()
        elif select == '2':
            print('填写运行测试参数\n ')
            params = str(input('输入参数：'))
            os.system(f'pytest {params}')
        elif select == '3':
            exit('退出成功')
        else:
            print('输入错误')


def save_cookies():
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get('https://test-cdpteatl9zu1.feishu.cn/admin/index')
    input('登录完成后输入任意字符保存cookies: ')
    cookies = driver.get_cookies()
    with open('cookies.yaml', 'w') as f:
        yaml.dump(cookies, f)
    print('\n保存cookies成功')


if __name__ == '__main__':
    main()
