# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/20
# File      ： wework_api
# IDE       ： PyCharm
import json

import requests


class WeWork:
    __corpsecret = "1GJ2IguAh0qpbDn2Occs45mB3jqsDNCRMQ14A5Xhaf8"
    __corpid = "ww0974c3188ad52760"
    __url = "https://qyapi.weixin.qq.com/cgi-bin/"

    def __init__(self):
        self.__access_token = ''

    def get_token(self):
        """
        获取access_token
        :return:
        """
        res = requests.get(self.__url + 'gettoken',
                           params={
                               "corpid": self.__corpid,
                               "corpsecret": self.__corpsecret
                           }
                           )
        self.__access_token = res.json()['access_token']

    def tag_list(self):
        """
        获取客户联系标签
        :return:
        """
        res = requests.post(
            self.__url + "externalcontact/get_corp_tag_list",
            params={"access_token": self.__access_token},
            json={}
        )
        return res

    def add(self, add_data, tag_name):
        """
        添加客户联系标签
        :param add_data: 添加标签的数据
        :param tag_name: 添加的标签的名字的集合
        :return:
        """
        res = requests.post(
            self.__url + "externalcontact/add_corp_tag",
            params={"access_token": self.__access_token},
            json=add_data
        )
        tag_list = self.tag_list().json()
        if res.json()['errcode'] == 0:
            for tag in tag_name:
                if tag not in json.dumps(tag_list, ensure_ascii=False):
                    raise Exception(f"添加{tag}失败")
            return True
        else:
            raise Exception("接口返回添加失败")

    def delete(self, tag_id, tag_id_list):
        """
        删除客户联系标签
        :param tag_id: 删除标签的id
        :param tag_id_list: 删除标签id的集合
        :return:
        """
        res = requests.post(
            self.__url + 'externalcontact/del_corp_tag',
            params={"access_token": self.__access_token},
            json=json.loads(json.dumps(tag_id))
        )
        tag_list = self.tag_list().json()
        if res.json()['errcode'] == 0:
            for tag in tag_id_list:
                if tag in json.dumps(tag_list, ensure_ascii=False):
                    raise Exception(f"删除{tag}失败")
            return True
        else:
            raise Exception("接口返回删除失败")

    def edit(self, edit_data):
        print(edit_data)
        res = requests.post(
            self.__url + 'externalcontact/edit_corp_tag',
            params={"access_token": self.__access_token},
            json=edit_data
        ).json()
        tag_list_res = self.tag_list().json()
        print(tag_list_res)
        if res['errcode'] == 0 and tag_list_res['errcode'] == 0:
            if edit_data['id'] not in json.dumps(tag_list_res, ensure_ascii=False):
                raise Exception(f"修改{edit_data['id']}失败")
            else:
                return True
        else:
            raise Exception("接口返回修改失败")

