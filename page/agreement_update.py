# 编辑合同_修改负责人
# 进入合同页面
import time
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class AgUpdate(BasePage):
    locator_agreement = (By.XPATH, "/html/body/div[1]/div/div/div[2]/ul[1]/li[7]/a")
    locator_a = (By.XPATH, '//form[@id="form1"]/table/tbody/tr/td[10]/a[2]')
    locator_person = (By.NAME, 'owner_role_name')
    locator_submit = (By.NAME, "submit")

    def agreement(self):
        self.driver.find_element(*self.locator_agreement).click()  # 点击合同

    def ele_a(self):
        self.driver.find_element(*self.locator_a).click()  # 点击第一个合同后面的编辑

    def ele_clear(self):
        self.driver.find_element(*self.locator_person).clear()  # 清空负责人默认信息

    def ele_person(self):
        self.driver.find_element(*self.locator_person).send_keys("admin")  # 点击第一个员工

    def ele_submit(self):
        self.driver.find_element(*self.locator_submit).click()  # 点击保存

    def update(self):
        self.agreement()  # 点击合同
        self.ele_a()     #点击第一个合同后面的编辑
        self.ele_clear()  # 清空内容
        self.ele_person()  # 负责人输入admin
        self.ele_submit()  # 点击保存
        time.sleep(2)
        result = self.driver.find_element(By.CLASS_NAME, 'alert alert-success').text  # 获取断言信息
        result = result.strip()
        return result
