import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://192.168.1.44/crm/index.php?m=user&a=login")
driver.find_element(By.NAME, "name").send_keys("admin")  # 点击第一个员工
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.NAME, "submit").click()
'''
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/ul[1]/li[7]/a").click()   #点击合同
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'btn-primary').click()  # 点击添加合同
time.sleep(2)
driver.find_element(By.NAME,'number').clear()
driver.find_element(By.NAME,'number').send_keys("00000001")#填写合同编号
driver.find_element(By.NAME,'business_name').click()#点击来源商机
time.sleep(2)
driver.find_elements_by_name('business')[1].click()     #点击第一个商机前的按钮
driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/button[1]').click()  #点击ok
driver.find_element(By.NAME, 'owner_role_name').clear()  # 点击负责人
driver.find_element(By.NAME, 'owner_role_name').send_keys('admin')
driver.find_element(By.NAME, "submit").click()  # 点击保存

'''

driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/ul[1]/li[7]/a").click()  # 点击合同

ele = driver.find_element(By.ID, 'field')   # 点击下拉框
Select(ele).select_by_value('number')  # 选择合同编号

element = driver.find_element(By.ID, 'condition')  # 点击下拉框
Select(element).select_by_value('start_with')  # 点击开始字符

driver.find_element(By.ID, 'search').send_keys("5k")  # 输入关键字
driver.find_element(By.XPATH, '//form[@id="searchForm"]/ul/li[4]/button').click()  # 点击搜索
driver.find_elements_by_class_name("check_list")[1].click()#点击第一个

driver.find_element(By.ID, 'delete').click()#点击删除
driver.switch_to.alert.text          #获取alert上的文本
driver.switch_to.alert.accept()