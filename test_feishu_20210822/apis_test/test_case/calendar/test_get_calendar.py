import random

import pytest

from apis_test.apis.calendar import Calendar
from apis_test.apis.fei_shu_api import FeiShuApi


class TestGetCalendar:
    def setup_class(self):
        fei_shu = FeiShuApi()
        self.calendar = Calendar(fei_shu.get_tenant_access_token())

    @pytest.mark.test_get_all_calendar
    def test_get_all_calendar(self):
        calendar_list = self.calendar.get_all_list()
        assert len(calendar_list) > 1

    @pytest.mark.test_get_calendar_for_page_size
    @pytest.mark.parametrize('page_size', [0, 49, 50, 51, 100, 499, 1000, 1001])
    def test_get_calendar_for_page_size(self, page_size):
        try:
            calendar_list = self.calendar.get_all_list(page_size)
            assert 1 < len(calendar_list) <= page_size
        except RuntimeError as e:
            # 当page_size 等于0， 49时 错误：code:99992402 错误信息：field validation failed 为正常结果
            if page_size in [0, 49, 1001] and str(e) == 'code:99992402 错误信息：field validation failed':
                pass
            else:
                raise e

    @pytest.mark.test_get_calendar_for_next_page
    def test_get_calendar_for_next_page(self):
        page_size = 50
        page_token = ''
        sync_token = ''
        try:
            while 1:
                data = self.calendar.get_all_res(page_size, page_token, sync_token)
                if data['data']['has_more']:
                    page_token = data['data']['page_token']
                    sync_token = data['data']['sync_token']
                else:
                    break
            pass
        except Exception as e:
            raise e

    @pytest.mark.test_search_calendar
    def test_search_calendar(self):
        res = self.calendar.search('测试日历')
        assert res.get('code') == 0

    @pytest.mark.test_get_calendar_detail
    def test_get_calendar_detail(self):
        random_id = self.calendar.get_random_calendar_id()
        res = self.calendar.get_calendar_for_id(random_id)
        assert res['data']['calendar_id'] == random_id
        assert len(res['data']) > 1
