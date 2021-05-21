# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/5/20
# File      ： test_tag
# IDE       ： PyCharm
import pytest
import yaml

from wework_api.wework_api import WeWork


class TestTag:
    def setup_class(self):
        self.we_work = WeWork()
        self.we_work.get_token()

    def test_tag_list(self):
        res = self.we_work.tag_list().json()
        print(res)
        assert res['errcode'] == 0

    @pytest.mark.parametrize('add_tag_data', yaml.safe_load(open('yaml_data/add_data.yaml', 'r')))
    def test_tag_add(self, add_tag_data):

        add_data = {}
        tag_name = []
        for k, v in add_tag_data.items():
            add_data = {"group_name": k, "tag": []}
            for val in v:
                tag_name.append(val)
                add_data['tag'].append(
                    {"name": val}
                )

        res = self.we_work.add(add_data, tag_name, 1)
        assert res

    @pytest.mark.parametrize('del_tag_data', yaml.safe_load(open('yaml_data/del_data.yaml', 'r')))
    def test_tag_del(self, del_tag_data):

        res = self.we_work.delete(del_tag_data)
        assert res

    @pytest.mark.parametrize('edit_data', yaml.safe_load(open('yaml_data/edit_data.yaml', 'r')))
    def test_tag_edit(self, edit_data):

        data = {
            "id": edit_data[0],
            "name": edit_data[1],
            "order": edit_data[2]
        }
        assert self.we_work.edit(data)

