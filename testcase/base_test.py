import unittest

from model.driver import Driver


class BaseTest(unittest.TestCase):

    def setUp(self):
        '''初始化浏览器对象'''
        print('初始化浏览器对象')
        self.driver = Driver().browser_chrome()

    def test_001(self):
        print(111)

    def tearDown(self):
        '''清理'''
        print('关闭浏览器')
        self.driver.quit()
# if __name__ == '__main__':
#     unittest.main()
