from __future__ import annotations

from apis_test.apis.fei_shu_api import FeiShuApi


class Events(FeiShuApi):
    def __init__(self, **kwargs):
        super().__init__()
        self.calendar_id = kwargs.get('calendar_id')

    def get(self) -> list(Events):
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{self.calendar_id}/events?anchor_time=1627818084'
        res = self.request(
            'get',
            url,
            # params={'anchor_time': '1627818084'}
        )
        print(res)
        events_list = []

        if res['code'] == 0 and 'items' in res['data']:
            for data in res['data']['items']:
                events_list.append(Events(**data))
        return events_list

    def create(self):
        data = {
            "summary": "日程标题",
            "description": "日程描述",
            "need_notification": False,
            "start_time": {
                "date": " 2018-09-01",
                "timestamp": "1605024000",
                "timezone": "Asia/Shanghai"
            },
            "end_time": {
                "date": " 2018-09-01",
                "timestamp": "1605024000",
                "timezone": "Asia/Shanghai"
            },
            "vchat": {
                "vc_type": "third_party",
                "icon_type": "vc",
                "description": "发起视频会议",
                "meeting_url": "https://example.com"
            },
            "visibility": "default",
            "attendee_ability": "can_see_others",
            "free_busy_status": "busy",
            "location": {
                "name": "地点名称",
                "address": "地点地址",
                "latitude": '116.350736',
                "longitude": '40.137436'
            },
            "color": -1,
            "reminders": [
                {
                    "minutes": 5
                }
            ],
            "recurrence": "FREQ=DAILY;INTERVAL=1",
            "schemas": [
                {
                    "ui_name": "ForwardIcon",
                    "ui_status": "hide",
                    "app_link": "xxxxx"
                }
            ]
        }
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{self.calendar_id}/events'
        res = self.request(
            'post',
            url,
            json=data
        )
        print(res)
        if res['code'] == 0:
            return True
        else:
            return False

