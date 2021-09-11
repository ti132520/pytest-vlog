import random
from selenium.webdriver.common.by import By
from ui_test.page.base_page import BasePage


class CalendarPage(BasePage):
    __ADD_CALENDAR_ICON_XPATH = '//*[@id="calendar-tab"]/div[1]/div/div[1]/div[5]/div[1]/div[2]/div/div/div'
    __CREATE_CALENDAR_XPATH = '//*[text()="新建日历"]'
    __SUMMARY_XPATH = '//*[@class="summary-input-adaptive"]/input'
    __BUTTON_CREATE_XPATH = '//*[text()="创建"]'
    __SELECT_PERMISSIONS_XPATH = '//*[@class="default-access-select row"]'
    __DESCRIPTION_XPATH = '//*[@class="calendar-description canEdit"]/*/textarea'

    __CALENDAR_GROUP_XPATH = '//*[@class="calendars-group"][1]//*[@class="calendar-item"]'
    __SETTING_ICON_XPATH = '//*[@class="larkc-svg-icon setting  "]'
    __BUTTON_SAVE_XPATH = '//*[text()="保存"]'

    def add_calendar(self, data):
        self.click_element(By.XPATH, self.__ADD_CALENDAR_ICON_XPATH)
        self.click_element(By.XPATH, self.__CREATE_CALENDAR_XPATH)
        self.send_data_element(By.XPATH, self.__SUMMARY_XPATH, data['summary'])
        if 'permissions' in data:
            self.click_element(By.XPATH, self.__SELECT_PERMISSIONS_XPATH)
            self.click_element(By.XPATH, f'//*[text()="{data["permissions"]}"]')
        if 'description' in data:
            self.send_data_element(By.XPATH, self.__DESCRIPTION_XPATH, data['description'])
        self.click_element(By.XPATH, self.__BUTTON_CREATE_XPATH)
        return CalendarPage(self.driver)

    def edit_calendar(self, summary):
        # 找到所有日历
        calendar_list = self.find_elements(By.XPATH, self.__CALENDAR_GROUP_XPATH)
        # 生成随机日历的位置
        random_num = random.randint(0, len(calendar_list) - 1)
        # 移动鼠标到选择的随机日历上
        self.move_to_element(calendar_list[random_num])
        self.click_element(By.XPATH, self.__SETTING_ICON_XPATH)
        self.send_data_element(By.XPATH, self.__SUMMARY_XPATH, summary)
        self.click_element(By.XPATH, self.__BUTTON_SAVE_XPATH)

    def search_calendar(self, summary):
        return self.find_element(By.XPATH, f'//*[text()="{summary}"]')
