import pytest

from apis_test.apis.calendar import Calendar


class TestCalendar:
    CALENDAR = None

    def setup_class(self):
        self.CALENDAR = Calendar()
        # self.CALENDAR.delete_all()

    @pytest.mark.test_list_of_no_calendar
    def test_list_of_no_calendar(self):
        calendars = self.CALENDAR.get()

        assert len(calendars) == 1

    @pytest.mark.parametrize("page_size", [0, 49, 50, 51, 499, 500, 501])
    def test_list_mass_calendar(self, page_size):
        self.CALENDAR.create('测试')
        calendars = self.CALENDAR.get(page_size)
        assert len(calendars) == page_size

    @pytest.mark.test_create
    def test_create(self):
        res = self.CALENDAR.create('测试日历', description=1, permissions='public', color='-1', summary_alias='1')
        assert res['code'] == 0

    @pytest.mark.test_calendar_events_list
    def test_calendar_events_list(self):
        calendar_list = self.CALENDAR.get_events(self.CALENDAR.get())
        print(calendar_list)

