from appium.webdriver.common.mobileby import MobileBy

from app_test.page.base_page import BasePage


class CalendarPage(BasePage):

    __by_add_calendar_lo = (MobileBy.XPATH, '//*[@resource-id="com.ss.android.lark:id/addCalendarIV"]')
    __by_create_calendar_lo = (MobileBy.XPATH, '//*[@text="新建日历"]')
    __by_summary_lo = (MobileBy.XPATH, '//*[@resource-id="com.ss.android.lark:id/calendarSummaryEditText"]')
    __by_save_lo = (MobileBy.XPATH, '//*[@text="保存"]')

    def add_calendar(self, data):

        self.click_element(self.__by_add_calendar_lo)
        self.click_element(self.__by_create_calendar_lo)
        self.send_element(self.__by_summary_lo, val=data['summary'])

        self.click_element(self.__by_save_lo)
        return CalendarPage(self.driver)
