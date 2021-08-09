from my_api.untils_test.api.api_base import ApiBase


class ApiTestCase(ApiBase):
    def get_case_list(self):
        res = self.request_method({'url': 'testcase', "method": "GET"})
        return res

    def get_case_for_id(self):
        data = self.get_case_list()
        if data.status_code == 200 and data.json()['code'] == 0:
            case_id = data.json()['data'][0]['id']
            return self.request_method({"url": f'testcase',
                                        "params": {"id": case_id}, "method": "GET"})
        else:
            raise Exception("没有数据")

    def post_case(self):
        data = {
            "nodeId": self.faker.name(),
            "remark": self.faker.user_name()
        }
        return self.request_method({
            'url': 'testcase',
            'method': "POST",
            'json': data
        })

    def put_case(self):
        data = self.get_case_list()
        if data.status_code == 200 and data.json()['code'] == 0:
            case_id = data.json()['data'][0]['id']
            data = {
                "id": case_id,
                "nodeId": self.faker.name(),
                "remark": self.faker.user_name()
            }
            return self.request_method({
                'url': 'testcase',
                'method': "PUT",
                'json': data
            })
        else:
            raise Exception("没有数据")

    def delete_case(self):
        data = self.get_case_list()
        if data.status_code == 200 and data.json()['code'] == 0:
            case_id = data.json()['data'][0]['id']
            return self.request_method({
                'url': 'testcase',
                'method': "DELETE",
                'json': {'id': case_id}
            })
        else:
            raise Exception("没有数据")
