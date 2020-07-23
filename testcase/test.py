import time
import unittest

from data.data_lib import get_txt
from model.driver import Driver
from page.login_page import LoginPage
from page.xs_page import XsPage
from testcase.base_test import BaseTest


class MyTestCase(BaseTest):

    # def setUp(self):
    #     print('111')
    #     self.driver = Driver().browser_chrome()
    #     print('ssss-',self.driver)

    def test_loginfont_suss(self):
        print('aaa')
        '''测试前台登录成功'''
        login = LoginPage(self.driver)  # 实例化loginPage类
        file_path = r'E:\PyCharm2020(64bit)\py_workspace\crm_selenium\data\data_text.txt'
        data = get_txt(file_path, 2)  # [[],[]]模式获取用户名密码
        u_name = data[0][0]
        password = data[0][1]
        actual = login.login(u_name, password)  # 调用login page的login方法
        # self.assertEqual('查询', actual)  # 断言
        xs = XsPage(self.driver)
        xs.xs()
        time.sleep(5)


# if __name__ == '__main__':
#     unittest.main()
