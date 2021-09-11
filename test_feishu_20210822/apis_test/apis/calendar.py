from __future__ import annotations
import logging
import random

from apis_test.apis.fei_shu_api import FeiShuApi

log = logging.getLogger()


class Calendar(FeiShuApi):
    __CALENDAR_URL = 'https://open.feishu.cn/open-apis/calendar/v4/calendars/'
    __CALENDAR_SEARCH_URL = 'https://open.feishu.cn/open-apis/calendar/v4/calendars/search'

    def __init__(self, token, **kwargs):
        self.token = token
        super().__init__(token)
        self.calendar_id = kwargs.get('calendar_id')
        self.color = kwargs.get('color')
        self.description = kwargs.get('description')
        self.permissions = kwargs.get('permissions')
        self.role = kwargs.get('role')
        self.summary = kwargs.get('summary')
        self.summary_alias = kwargs.get('summary_alias')
        self.type = kwargs.get('type')

    def create(self, json):
        res = self.request(
            'post',
            self.__CALENDAR_URL,
            json=json
        )
        return res

    def update(self, calendar_id, json):
        res = self.request(
            'patch',
            self.__CALENDAR_URL + calendar_id,
            json=json
        )
        return res

    def get_all_res(self, page_size: int = 50, page_token: str = None, sync_token: str = None):
        """
        获取所有日历 接口返回直接返回
        :param page_token: 上一页token
        :param sync_token: 下一页token
        :param page_size: 分片大小
        :return: 日历的list
        ->是返回值的注释
        """
        params = {'page_size': page_size}
        if page_token: params['page_token'] = page_token
        if sync_token: params['sync_token'] = sync_token

        res = self.request(
            'get',
            self.__CALENDAR_URL,
            params=params
        )
        return res

    def search(self, query: str = '', page_size: int = 50, page_token: str = None):
        params = {'page_size': page_size}
        if page_token:
            params['page_token'] = page_token
        res = self.request('post', self.__CALENDAR_SEARCH_URL, json={'query': query}, params=params)
        return res

    def get_calendar_for_id(self, calendar_id):
        return self.request(
            'get',
            self.__CALENDAR_URL + calendar_id
        )

    def get_random_calendar_id(self):
        """
        随机获取有一个日历
        :return:
        """
        calendar_list = self.get_all_list()
        calendar_id = [calendar.calendar_id for calendar in calendar_list]
        random_num = random.randint(1, len(calendar_id))
        return calendar_id[random_num]

    def get_all_list(self, page_size: int = 50, page_token: str = None, sync_token: str = None) -> list[Calendar]:
        """
        获取所有日历的列表
        :param sync_token: 上一页token
        :param page_token: 下一页token
        :param page_size: 分片大小
        :return: 日历的list
        ->是返回值的注释
        """
        params = {'page_size': page_size}
        if page_token: params['page_token'] = page_token
        if sync_token: params['sync_token'] = sync_token
        res = self.request(
            'get',
            self.__CALENDAR_URL,
            params=params
        )
        calendar_list: list[Calendar] = []
        if res['code'] == 0:
            for data in res['data']['calendar_list']:
                calendar_list.append(Calendar(self.token, **data))

        return calendar_list

    def delete(self, calendar_id=None):
        if calendar_id is None:
            calendar_id = self.calendar_id
        res = self.request('delete', self.__CALENDAR_URL + calendar_id)
        return res

    def delete_all(self):
        """
        删除所有（保留49条）
        :return: null
        """
        for item, key in self.get_all_list():
            if key > 48 and item.type != 'primary':
                item.delete()
