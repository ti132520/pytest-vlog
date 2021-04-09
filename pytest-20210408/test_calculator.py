import pytest
import yaml

from Calculator import Calculator


class TestCal:
    @staticmethod
    def setup_class():
        print('开始测试')

    @staticmethod
    def teardown_class():
        print('测试结束')

    # 方法执行前
    def setup(self):
        print('计算开始')
        self.cal = Calculator()

    # 方法执行后
    @staticmethod
    def teardown():
        print('计算结束')

    # pytest
    @pytest.mark.test_add
    @pytest.mark.parametrize('a,b', [
        [1, 2], [2, 3]
    ], ids=['one', 'two'])
    # 测试用例：计算器加法测试
    def test_add(self, a, b):
        assert self.cal.add_fun(a, b) in [3, 5]

    @pytest.mark.parametrize('a,b', [
        [1, 1], [3, 3]
    ])
    # 测试用例：计算器除法测试
    def test_div(self, a, b):
        assert self.cal.div_fun(a, b) == 1

    # yaml 参数导入1
    @pytest.mark.parametrize('par', yaml.load(open('./par.yaml', 'r'), Loader=yaml.FullLoader))
    def test_yaml_add(self, par):
        assert self.cal.add_fun(par[0], par[1]) in [3, 5, 7]

    # yaml 参数导入2
    @pytest.mark.parametrize('a,b', yaml.load(open('./par.yaml', 'r'), Loader=yaml.FullLoader))
    def test_yaml_add2(self, a, b):
        assert self.cal.add_fun(a, b) in [3, 5, 7]
