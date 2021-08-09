from faker import Faker
import requests


class ApiBase:
    base_url = 'http://127.0.0.1:8000/'
    faker = Faker(locale="zh_CN")

    def request_method(self, data):
        data['url'] = self.base_url + data['url']
        return requests.request(**data)

