# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/16
# File      ： quotation
# IDE       ： PyCharm
import time

from page.base_page import BasePage


class QuotationPage(BasePage):

    def edit_name_with_more(self, data):
        if data:
            for k, v in data.items():
                print(k)
                print(v)
            time.sleep(5)
            return 1
        else:
            return Exception("没有传入要改的数据")
