# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/28
# File      ： test_chongqinnetmp
# IDE       ： PyCharm
from page.mp import Mp


class TestCase:

    def setup_class(self):
        self.obj = Mp()

    def teardown_method(self):
        self.obj.restart()

    def test_search(self):
        self.obj.start().goto_mp().goto_search().search_keyword('分享')
