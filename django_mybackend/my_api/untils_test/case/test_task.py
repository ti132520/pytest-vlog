from my_api.untils_test.api.api_task import ApiTask


class TestTask:
    __api = ApiTask()

    @staticmethod
    def __asert_default(res):
        assert res.status_code == 200
        assert res.json()['code'] == 0

    def test_get_task(self):
        res = self.__api.get_task_list()
        self.__asert_default(res)

    def test_get_task_for_id(self):
        res = self.__api.get_task_for_id()
        self.__asert_default(res)
