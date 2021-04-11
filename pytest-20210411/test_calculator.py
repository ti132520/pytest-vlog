import pytest


@pytest.fixture(scope='class', autouse=True)
def init_class():
    print('开始测试 class 级别输出')
    yield
    print('测试结束 class 级别输出')


@pytest.fixture(scope='session', autouse=True)
def init_session():
    print('开始测试 session 级别输出')
    yield
    print('测试结束 session 级别输出')


class TestCal:
    # pytest
    @pytest.mark.test_add
    @pytest.mark.parametrize('a,b', [
        [1, 2], [2, 3]
    ], ids=['one', 'two'])
    # 测试用例：计算器加法测试
    def test_add(self, init_calculator_fun, a, b):
        assert init_calculator_fun.add_fun(a, b) in [3, 5]

    @pytest.mark.parametrize('a,b', [
        [1, 1], [3, 3]
    ], ids=['计算器加法测试1', '计算器加法测试2'])
    # 测试用例：计算器除法测试
    @pytest.mark.run(2)
    def test_div(self, init_calculator_fun, a, b):
        assert init_calculator_fun.div_fun(a, b) == 1

    # yaml 参数导入1
    @pytest.mark.run(0)
    def test_yaml_add(self, init_calculator_fun, init_calculator_data):
        assert init_calculator_fun.add_fun(init_calculator_data[0], init_calculator_data[1]) > 0

    # yaml 参数导入2
    @pytest.mark.second
    def test_yaml_add2(self, init_calculator_fun, init_calculator_data):
        assert init_calculator_fun.add_fun(init_calculator_data[0], init_calculator_data[1]) > 0
