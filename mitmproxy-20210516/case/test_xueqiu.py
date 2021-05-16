# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/16
# File      ： test_xueqiu
# IDE       ： PyCharm
from page.app import App


class TestXueQiu:
    def setup_class(self):
        self.app = App()
        self.app.start()

    def teardown_method(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    def test_quote(self):
        data = {'name': '爱', 'percent': 0}

        assert self.app.goto_main().goto_quotation().edit_name_with_more(data=data)

