'''
登录测试用例执行
'''
from page.login_page import LoginPage
from testcase.base_test import BaseTest
from data.data_lib import get_txt
from model.driver import Driver
import unittest

class LoginTestCase(unittest.TestCase):

    def setUP(self):
        '''初始化，实例化浏览器对象'''
        # self.driver = Driver().browser_chrome()
        # print('ssss-',self.driver)
        print('初始化')

    def test_loginfont_suss(self):
        '''测试前台登录成功'''
        login = LoginPage(self.driver)  #实例化loginPage类
        file_path = r'E:\PyCharm2020(64bit)\py_workspace\crm_selenium\data\data_text.txt'
        data = get_txt(file_path,2) #[[],[]]模式获取用户名密码
        u_name = data[0][0]
        password = data[0][1]
        actual = login.login(u_name,password)   #调用login page的login方法
        self.assertEqual(u_name, actual)    #断言

if __name__ == '__main__':
    unittest.main()