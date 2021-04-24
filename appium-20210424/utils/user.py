# -*- coding: utf-8 -*-  
# Author    ： 怕你呀
# Time      ： 2021/4/24
# File      ： user
# IDE       ： PyCharm
from faker import Faker


class User:
    def __init__(self):
        self.faker = Faker("zh-CN")

    def get_name(self):
        return self.faker.name()

    def get_phone(self):
        return self.faker.phone_number()


if __name__ == '__main__':
    pr = User().get_phone()
    print(pr)
