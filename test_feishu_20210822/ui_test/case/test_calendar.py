import random
import time

import pytest
from faker import Faker

from ui_test.page.main_page import MainPage
faker = Faker(locale='zh-CN')


class TestCalendarWeb:
    web = None

    def setup_class(self):
        self.web = MainPage()

    def teardown_class(self):
        self.web.quit()

    @pytest.mark.parametrize("data", [
        {'summary': faker.name(), 'permissions': random.choice(['私密', '仅显示忙碌', '公开']),
         'color': -1, 'summary_alias': faker.name()},
        {'summary': faker.name(), 'description': faker.text(50),
         'color': -1, 'summary_alias': faker.name()},
        {'summary': faker.name(), 'description': faker.text(50),
         'permissions': random.choice(['私密', '仅显示忙碌', '公开']),
         'color': -1},
        {'summary': faker.name(), 'description': faker.text(50)},
        {'summary': faker.name(), 'summary_alias': faker.name()},
        {'summary': faker.name(), 'description': faker.text(50),
         'permissions': random.choice(['私密', '仅显示忙碌', '公开']),
         'color': -1, 'summary_alias': faker.name()},
        {'summary': faker.name(), 'description': faker.text(50),
         'summary_alias': faker.name()},
    ])
    @pytest.mark.test_add_calendar
    def test_add_calendar(self, data):
        self.web.goto_calendar().add_calendar(data)
        assert self.web.goto_calendar().search_calendar(data['summary'])

    @pytest.mark.test_edit_calendar
    def test_edit_calendar(self):
        edit_summary = faker.name()
        self.web.goto_calendar().edit_calendar(edit_summary)
        assert self.web.goto_calendar().search_calendar(edit_summary)

