import random

import pytest
from faker import Faker

from apis_test.apis.calendar import Calendar
from apis_test.apis.fei_shu_api import FeiShuApi

faker = Faker(locale="zh-CN")


class TestCalendarEdit:

    def setup_class(self):
        fei_shu = FeiShuApi()
        self.calendar = Calendar(fei_shu.get_tenant_access_token())

    @pytest.mark.test_default_create
    def test_default_create(self):
        summary = Faker().name()
        create_res = self.calendar.create({'summary': summary})
        calendar_detail = self.calendar.get_calendar_for_id(create_res['data']['calendar']['calendar_id'])
        assert create_res['code'] == 0
        assert calendar_detail['code'] == 0
        assert calendar_detail['data']['summary'] == summary

    @pytest.mark.parametrize('data', [
        {'summary': faker.name(), 'permissions': random.choice(['public', 'show_only_free_busy', 'private']),
         'color': -1, 'summary_alias': faker.name()},
        {'summary': faker.name(), 'description': faker.text(50),
         'color': -1, 'summary_alias': faker.name()},
        {'summary': faker.name(), 'description': faker.text(50),
         'permissions': random.choice(['public', 'show_only_free_busy', 'private']),
         'color': -1},
        {'summary': faker.name(), 'description': faker.text(50)},
        {'summary': faker.name(), 'summary_alias': faker.name()},
        {'summary': faker.name(), 'description': faker.text(50),
         'permissions': random.choice(['public', 'show_only_free_busy', 'private']),
         'color': -1, 'summary_alias': faker.name()},
        {'summary': faker.name(), 'description': faker.text(50),
         'summary_alias': faker.name()},
    ])
    @pytest.mark.test_params_create
    def test_params_create(self, data):
        create_res = self.calendar.create(data)
        calendar_detail = self.calendar.get_calendar_for_id(create_res['data']['calendar']['calendar_id'])
        assert create_res['code'] == 0
        assert calendar_detail['code'] == 0
        assert calendar_detail['data']['summary'] == data['summary']

    @pytest.mark.test_update_calendar
    def test_update_calendar(self):
        calendar_list = self.calendar.get_all_list()
        calendar_id = [calendar.calendar_id for calendar in calendar_list]
        random_num = random.randint(1, len(calendar_id))
        random_id = calendar_id[random_num]
        update_data = {'summary': faker.name(), 'permissions': random.choice(['public', 'show_only_free_busy', 'private']),
         'color': -1, 'summary_alias': faker.name()}
        res = self.calendar.update(calendar_id=random_id, json=update_data)
        assert res['code'] == 0

    @pytest.mark.test_delete_calendar
    def test_delete_calendar(self):
        calendar_list = self.calendar.get_all_list()
        calendar_id = [calendar.calendar_id for calendar in calendar_list]
        random_num = random.randint(1, len(calendar_id))
        random_id = calendar_id[random_num]
        res = self.calendar.delete(calendar_id=random_id)
        assert res['code'] == 0


