from apis_test.apis.base_api import BaseApi


class FeiShuApi(BaseApi):
    __APP_ID: str = 'cli_a1ab4f10f3f8900c'
    __APP_SECRET: str = 'KO4gsSWpO2jsEYZx8P8X9cBS0HZbheDd'

    def __init__(self):
        self.get_token()

    def get_token(self):
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
        if self.ACCESS_TOKEN is None:
            res = self.request('get', url, json={
                "app_id": self.__APP_ID,
                "app_secret": self.__APP_SECRET
            })
            self.ACCESS_TOKEN = res['tenant_access_token']
        return self.ACCESS_TOKEN

