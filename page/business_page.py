'''商机页面'''
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class BusinessPage(BasePage):
    #定位器
    locator_home_business = (By.XPATH, '//div[@class="container"]/div[2]/ul[1]/li[3]/a')
    locator_add_business = (By.XPATH,'//div[@class="row"]/div[1]/div/a')
    locator_customer_name = (By.ID,'customer_name')
    locator_customer = (By.NAME,'customer')
    locator_confirm_add_cus = (By.CSS_SELECTOR,'div[id="dialog-message"]+div>div button:nth-child(1)>span')
    locator_business_name = (By.ID,'name')
    locator_business_price = (By.ID,'estimate_price')
    locator_confirm_business = (By.XPATH,'//form[@id="form1"]/table/tfoot/tr/td/input[1]')

    def home_business(self):
        '''点击商机进入'''
        action = self.find_element(self.locator_home_business)
        action.click()

    def add_business(self):
        '''点击添加商机'''
        action = self.find_element(self.locator_add_business)
        action.click()

    def create_business_cusname(self):
        '''添加客户名称，跳转至选择客户'''
        action = self.find_element(self.locator_customer_name)
        action.click()

    def select_customer(self):
        '''选择客户'''
        self.driver.find_elements(*self.locator_customer)[0].click()

    def add_customer(self):
        '''确认添加客户'''
        action = self.find_element(self.locator_confirm_add_cus)
        action.click()

    def business_name(self,bname):
        action = self.find_element(self.locator_business_name)
        action.send_keys(bname)

    def business_price(self,price):
        action = self.find_element(self.locator_business_price)
        action.send_keys(price)

    def confirm_business(self):
        action = self.find_element(self.locator_confirm_business)
        action.click()

    def business_flow(self,bname,price):
        '''添加商机流程'''
        self.home_business()
        self.add_business()
        self.create_business_cusname()
        self.select_customer()
        self.add_customer()
        self.business_name(bname)
        self.business_price(price)
        self.confirm_business()
