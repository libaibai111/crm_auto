'''
线索page
'''
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class XsPage(BasePage):

    loc_xs = (By.LINK_TEXT, '线索')

    def xs_xs(self):
        self.find_element(self.loc_xs).click()

    def xs(self):
        self.xs_xs()