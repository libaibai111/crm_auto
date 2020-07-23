'''
客户page
'''
import time

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ClientPage(BasePage):

    #定位器
    loc_client_inlet = (By.LINK_TEXT, '客户') #客户功能入口
    loc_create_client = (By.CSS_SELECTOR,'a.btn.btn-primary' )  #创建客户入口按钮
    #创建客户页面
    loc_client_name = (By.NAME, 'name') #客户名称
    loc_create_business1 = (By.NAME, 'create_business1')    #同时创建商机单选框
    loc_preserve_submit = (By.XPATH, '//form1[@id="form1"]/table/tfoot/tr/td/input[1]') #保存按钮
    loc_assert = (By.XPATH, '//form[@id="form1"]/table/tbody/tr[1]/td[3]/a/span')   #断言

    def client_inlet(self):
        '''客户功能入口按钮'''
        self.find_element(self.loc_client_inlet).click()

    def create_client_butt(self):
        '''创建客户入口按钮'''
        self.find_element(self.loc_create_client).click()

    def client_name(self, cname):
        '''客户名称输入框'''
        self.find_element(self.loc_client_name).clear()
        self.find_element(self.loc_client_name).send_keys(cname)

    def create_business1(self):
        '''同时创建商机'''
        self.find_element(self.loc_create_business1).click()

    def preserve_submit(self):
        '''保存按钮'''
        self.find_element(self.loc_preserve_submit).click()

    def client(self, cname):
        '''创建客户功能实现'''
        self.client_inlet()
        time.sleep(3)
        self.create_client_butt()
        self.client_name(cname)
        self.preserve_submit()
        ret = self.assert_result(self.loc_assert)

        return ret
