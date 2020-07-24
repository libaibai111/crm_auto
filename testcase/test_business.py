import unittest
from data.data_lib import get_txt
from page.business_page import BusinessPage
from page.login_page import LoginPage
from testcase import base_test


class BusinessTestCase(base_test.BaseTest):
    def test_business_add(self):
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
        busy.home_business()
        busy.add_business()
        busy.business_add_flow(0,'yiyi','140')

    def test_business_aedit(self):
        '''编辑商机'''
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
        busy.home_business()
        busy.edit_business()
        busy.business_edit_flow(0, 'lily', '233')

    def test_business_asearch(self):
        '''搜索商机'''
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
        busy.home_business()
        busy.business_search_flow('name','contains','l')

    def z_all_business_delete(self):
        '''删除全部商机'''
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
        busy.home_business()
        busy.delete_business_all()

    def test_part_business_delete(self):
        '''选择删除商机'''
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
        busy.home_business()
        busy.delete_business_sel(0)



if __name__ == '__main__':
    unittest.main()
