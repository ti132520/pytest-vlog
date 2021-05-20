# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/16
# File      ： mitmdump_xueqiu
# IDE       ： PyCharm
import json

import mitmproxy.http
from mitmproxy import http


class Events:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and "x=" in flow.request.url:
            data = flow.response.text
            data = recursion(json.loads(data), 0)
            flow.response.text = json.dumps(data)
            # flow.response = http.HTTPResponse.make(
            #     200,
            #     json.dumps(data),
            # )
        """

        :param flow:
        :return:
        """


def recursion(data, multiple=1):
    """
    递归倍增浮点数据
    :param data: 数据
    :param multiple: 倍增的倍数
    :return: 返回处理后的数据
    """
    if isinstance(data, dict):
        for k, v in data.items():
            if k == 'name':
                v = 'ai'
            data[k] = recursion(v, multiple)
    if isinstance(data, list):

        # data_new = []
        # for i in data:
        #     data_new.append(recursion(i, multiple))
        # data = data_new
        data = [recursion(i, multiple) for i in data]

    if isinstance(data, float):
        data = data * multiple

    else:
        data = data

    return data


addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8080', '-s', __file__])
