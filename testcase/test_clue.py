import unittest
from page.clue_page import CluePage
from page.login_page import LoginPage
from testcase.base_test import BaseTest

class ClueTestCase(BaseTest):
    def test_clue(self):
        '''添加线索转换为客户'''
        login = LoginPage(self.driver)  # 实例化loginPage类
        u_name = 'admin'
        password = 'admin123'
        contact = '李先生'
        customer = '李白白'
        login.login(u_name, password)  # 调用login page的login方法

        clue = CluePage(self.driver)  # 调用clue_page

        text = clue.ele_clue(contact,customer)  # 调用clue_page的ele_clue方法

        self.assertIn("添加客户成功", text)
if __name__ == '__main__':
    unittest.main()