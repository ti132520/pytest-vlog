import logging

from my_api.untils_test.api.api_base import ApiBase


class ApiTask(ApiBase):
    def get_task_list(self):
        return self.request_method({
            "method": "GET",
            "url": "task"
        })

    def get_task_for_id(self):
        data = self.get_task_list()
        if data.status_code == 200 and data.json()['code'] == 0:
            return self.request_method({
                "method": "GET",
                "url": "task",
                "params": {
                    "id": data.json()['data'][0]['id']
                }
            })

        else:
            raise Exception("没有数据")
