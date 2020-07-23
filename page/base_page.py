'''
页面类基类
'''
from model.driver import Driver

class BasePage():

    def __init__(self, driver):
        '''初始化，实例化浏览器驱动对象'''
        self.driver = driver
        self.url = 'http://localhost/crm/index.php?m=user&a=login'   #定义url
        self.timeout = 5

    def open(self):
        '''
        打开url
        :return:
        '''
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.timeout)   #设置隐式等待

    def find_element(self, loc):
        '''元素定位'''
        return self.driver.find_element(*loc)

    def close_browser(self):
        '''关闭浏览器和浏览器驱动'''
        self.driver.quit()

    def assert_result(self, loc):
        '''
        断言信息获取'
        :param loc: 元素定位信息
        :return: 断言文本信息
        '''
        ret = self.find_element(loc).text
        print(ret)
        return ret


