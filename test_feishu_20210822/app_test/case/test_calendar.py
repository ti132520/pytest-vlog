import random

from faker import Faker
import pytest

from app_test.page.app import App
faker = Faker()


class TestCalendar:

    def setup_class(self):
        self.driver = App()
        self.app = self.driver.restart().goto_main().goto_calendar()

    def teardown_class(self):
        self.driver.stop()

    @pytest.mark.parametrize("test_data", [
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
    @pytest.mark.test_app_calendar
    def test_app_calendar(self, test_data):
        self.app.add_calendar(test_data)
        find_ele = self.app.swipe_find_element(test_data['summary'])
        assert find_ele.text == test_data['summary']

