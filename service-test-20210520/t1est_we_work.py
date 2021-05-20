# -*- coding: utf-8 -*-
# Author    ： 怕你呀
# Time      ： 2021/5/20
# File      ： test_we_work
# IDE       ： PyCharm



def get_data(url, params):

    if res.status_code == 200:
        return res.json()
    else:
        return False


class TestWeWork:
    def setup_class(self):
        res = get_data('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                       params={
                           "corpid": "ww0974c3188ad52760",
                           "corpsecret": "1GJ2IguAh0qpbDn2Occs45mB3jqsDNCRMQ14A5Xhaf8"
                       }
                       )
        self.access_token = res['access_token']

    def test_get_token(self):
        print(self.access_token)

    def test_get_tag(self):
        print(self.access_token)
