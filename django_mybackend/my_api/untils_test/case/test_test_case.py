from my_api.untils_test.api.api_test_case import ApiTestCase


class TestTestCase:
    __api = ApiTestCase()

    @staticmethod
    def __asert_default(res):
        assert res.status_code == 200
        assert res.json()['code'] == 0

    def test_get_case(self):
        res = self.__api.get_case_list()
        self.__asert_default(res)

    def test_get_case_for_id(self):
        res = self.__api.get_case_for_id()
        self.__asert_default(res)

    def test_post_case(self):
        res = self.__api.post_case()
        self.__asert_default(res)

    def test_put_case(self):
        res = self.__api.put_case()
        self.__asert_default(res)

    def test_delete_case(self):
        res = self.__api.delete_case()
        self.__asert_default(res)
