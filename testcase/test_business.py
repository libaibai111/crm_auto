import unittest
from data.data_lib import get_txt
from page.business_page import BusinessPage
from page.login_page import LoginPage
from testcase import base_test


class BusinessTestCase(base_test.BaseTest):
    def test_business(self):
        '''添加商机流程'''
        print('aaa')
        '''测试前台登录成功'''
        login = LoginPage(self.driver)  # 实例化loginPage类
        file_path = r'E:\auto\crm_auto\data\data_text.txt'
        data = get_txt(file_path, 2)  # [[],[]]模式获取用户名密码
        u_name = data[0][0]
        password = data[0][1]
        actual = login.login(u_name, password)  # 调用login page的login方法
        self.assertEqual(u_name, actual)  # 断言
        busy = BusinessPage(self.driver)
        busy.business_flow('wowo','120')


if __name__ == '__main__':
    unittest.main()
