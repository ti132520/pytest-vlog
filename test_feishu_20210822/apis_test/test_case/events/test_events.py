from apis_test.apis.calendar import Calendar
from apis_test.apis.events import Events
import pytest


class TestEvents:

    def setup_class(self):
        self.CALENDAR = Calendar()

    @pytest.mark.test_event_create
    def test_create(self):
        calendar_list = self.CALENDAR.get()
        for item in calendar_list:
            Events(calendar_id=item.calendar_id).create()
