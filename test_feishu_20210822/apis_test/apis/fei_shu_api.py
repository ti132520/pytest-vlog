from apis_test.apis.http_api import HttpApi


class FeiShuApi(HttpApi):
    __APP_ID: str = 'cli_a1ab4f10f3f8900c'
    __APP_SECRET: str = 'KO4gsSWpO2jsEYZx8P8X9cBS0HZbheDd'
    __TOKEN = {}

    def __init__(self, token: dict = {}):
        self.__TOKEN = token

    def request(self, method, url, **kwargs):
        if 'headers' in kwargs:
            kwargs['headers']['Content-Type'] = 'application/json; charset=utf-8'
        else:
            kwargs['headers'] = {'Content-Type': 'application/json; charset=utf-8'}
        if self.__TOKEN.get('tenant_access_token'):
            kwargs['headers']['Authorization'] = f'Bearer {self.__TOKEN["tenant_access_token"]}'
        return super().http_request(method, url, **kwargs)

    def get_tenant_access_token(self):
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'

        res = self.request('get', url, json={
            "app_id": self.__APP_ID,
            "app_secret": self.__APP_SECRET
        })
        return {'tenant_access_token': res['tenant_access_token']}
