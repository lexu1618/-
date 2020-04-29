from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageLocators.indexpage_locator import IndexPageLocator as loc
import random


class IndexPage:
    def __init__(self,driver):
        self.driver =driver

    def isExist_login_ele(self):
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.logout_button))
            return True
        except:
            return False




    #选标操作  默认选第一个， 元素定位时过滤掉不可以投的标
    def click_first_bid(self):
        WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located((loc.bid_button)))
        self.driver.find_elements(*loc.bid_button).click()



    #随机选一个标
    def click_bid_random(self):
        #找到所有符合的标
        eles = self.driver.find_elements()
        #随机数
        index = random.randint(0,len(eles)-1)
        eles[index].click()