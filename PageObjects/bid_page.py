from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PageLocators.bigpage_locator import BigPageLocators as loc
from Common.basepage import BasePage



class BidPage(BasePage):

    # def __init__(self,driver):
    #     self.driver = driver

    #投资
    def invest(self,monkey):
        #输入框输入金额
        # WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located((loc.monkey_input)))
        # self.driver.find_element(*loc.monkey_input).send_keys(monkey)
        doc = "标详情页面_投资操作"
        self.wait_eleVisible(loc.monkey_input,doc)
        self.inpput_text(loc.monkey_input,monkey,doc)
        # 点击投标按钮
        # self.driver.find_element(*loc.active_button_on_successPop).click()
        self.click_element(loc.monkey_input,doc)


    #获取用户余额
    def get_user_monkey(self):
        WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located((loc.monkey_input)))
        return self.driver.find_element(*loc.monkey_input).get_attribute("data-mount")

    #获取投资前用户余额
    def get_user_monkey_invest(self):
        pass

    #投资成功的提示框 ---点击查看并激活
    def click_activeButton_on_success_popup(self):
        WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located((loc.active_button_on_successPop)))
        self.driver.find_element(*loc.active_button_on_successPop).click()

    #错误提示框  --页面中间   必须为100的整数    请正确填写投标金额
    def get_errorMsg_from_pageCenter(self):

        #获取文本内容
        WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located((loc.invest_failed_popup_button)))
        msg = self.driver.find_element(*loc.invest_failed_popup_button).text
        #关闭弹窗
        self.driver.find_element(*loc.invest_close_failed_popup_button).click()
        return msg

        pass

    #获取提示信息  ---投标按钮上的
    def get_errorMsg_from_investButton(self):
        pass