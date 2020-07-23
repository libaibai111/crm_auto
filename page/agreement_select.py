from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page.base_page import BasePage


class AgSelect(BasePage):
    locator_agreement = (By.XPATH, "/html/body/div[1]/div/div/div[2]/ul[1]/li[7]/a")
    locator_keyword = (By.ID, 'search')
    locator_select = (By.CLASS_NAME, 'btn')

    def agreement(self):
        self.driver.find_element(*self.locator_agreement).click()  # 点击合同

    def ele_cli(self):
        element = self.driver.find_element(By.ID, 'field').click()  # 点击下拉框
        Select(element).select_by_value('number')  # 选择合同编号

    def ele_cli2(self):
        element = self.driver.find_element(By.ID, 'condition').click()  # 点击下拉框
        Select(element).select_by_value('start_with')  # 点击开始字符

    def ele_keyword(self):
        self.driver.find_element(*self.locator_keyword).send_keys("5k")  # 输入关键字

    def ele_select(self):
        self.driver.find_element(*self.locator_select).click()  # 点击搜索

    def select(self):
        self.agreement()   # 点击合同
        self.ele_cli()      # 点击下拉框选择合同
        self.ele_cli2()     # 点击下拉框选择开始字符
        self.ele_keyword()      # 输入关键字
        self.ele_select()       # 点击搜索

