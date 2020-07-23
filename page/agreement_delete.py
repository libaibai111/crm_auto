from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page.base_page import BasePage

class AgDelete(BasePage):
    locator_agreement = (By.XPATH, "/html/body/div[1]/div/div/div[2]/ul[1]/li[7]/a")
    locator_xia1 = (By.ID, 'field')
    locator_xia2 =(By.ID, 'condition')
    locator_guanjian = (By.ID, 'search')
    def agreement(self):
        self.driver.find_element(*self.locator_agreement).click()  # 点击合同

    def ele_xiala1(self):
        e = self.driver.find_element(*self.locator_xia1)   # 点击下拉框
        Select(e).select_by_value('number')  # 选择合同编号

    def ele_xiala2(self):
        el = self.driver.find_element(*self.locator_xia2)  # 点击下拉框
        Select(el).select_by_value('start_with')  # 点击开始字符
    def ele_guanjian(self):
        driver.find_element(*self.locator_guanjian).send_keys("5k")  # 输入关键字
        driver.find_element(By.XPATH, '//form[@id="searchForm"]/ul/li[4]/button').click()  # 点击搜索
        driver.find_elements_by_class_name("check_list")[1].click()#点击第一个

        driver.find_element(By.ID, 'delete').click()#点击删除
        driver.switch_to.alert.text          #获取alert上的文本
        driver.switch_to.alert.accept()         #点击确定











#删除合同
#进入合同页面
element = driver.find_element(By.CLASS_NAME,'check_list').click()#选择第一个合同
element = driver.find_element(By.ID,'delete').click()#点击删除
#点击退出