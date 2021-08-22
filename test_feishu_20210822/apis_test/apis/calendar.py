from __future__ import annotations

from apis_test.apis.events import Events
from apis_test.apis.fei_shu_api import FeiShuApi


class Calendar(FeiShuApi):
    __CALENDAR_URL = 'https://open.feishu.cn/open-apis/calendar/v4/calendars/'

    def __init__(self, **kwargs):
        super().__init__()
        self.calendar_id = kwargs.get('calendar_id')
        self.color = kwargs.get('color')
        self.description = kwargs.get('description')
        self.permissions = kwargs.get('permissions')
        self.role = kwargs.get('role')
        self.summary = kwargs.get('summary')
        self.summary_alias = kwargs.get('summary_alias')
        self.type = kwargs.get('type')

    def create(self, summary, **kwargs):
        kwargs['summary'] = summary
        res = self.request(
            'post',
            self.__CALENDAR_URL,
            json=kwargs
        )
        return res

    def get(self, page_size: int = 50) -> list[Calendar]:
        res = self.request(
            'get',
            self.__CALENDAR_URL,
            params={
                'page_size': page_size
            }
        )
        print(res)
        calendar_list: list[Calendar] = []
        if res['code'] == 0:
            for data in res['data']['calendar_list']:
                calendar_list.append(Calendar(**data))
        return calendar_list

    def delete(self, calendar_id=None):
        if calendar_id is None:
            calendar_id = self.calendar_id
        res = self.request('delete', self.__CALENDAR_URL + calendar_id)
        return res

    def delete_all(self):
        for item in self.get():
            if item.type != 'primary':
                item.delete()

    def get_events(self, calendar_list):
        events_list = []
        for item in calendar_list:
            calendar_id = item.calendar_id
            events_list_res = Events(calendar_id=calendar_id).get()
            if events_list_res:
                events_list.append(events_list_res)
        return events_list
