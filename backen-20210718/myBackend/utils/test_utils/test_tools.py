import logging

from ..jenkins_api_tools import Tools


class TestTools:
    def test_get_jobs(self):
        res = Tools.get_jobs()
        assert res

    def test_invoke(self):
        res = Tools.invoke('test')
        print(res)
