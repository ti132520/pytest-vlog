# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/14
# File      ： test_search
# IDE       ： PyCharm
import pytest

from page.web import Web


class TestSearch:
    def setup_class(self):
        self._instance = Web()
        self._instance.start()

    def teardown_method(self):
        self._instance.restart()

    def teardown_class(self):
        self._instance.stop()

    @pytest.mark.parametrize('a', [0, 1])
    def tes1t_search(self, a):
        assert self._instance.goto_main().get_att() == '百度一下'

    def test_get_handles(self):
        print(self._instance.goto_main().get_handles())

