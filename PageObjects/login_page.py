from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.loginpage_locator import LoginPageLocator as loc
from Common.basepage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    #登录
    def login(self,username,password,remeber_user=True):
        #输入用户名
        #输入密码
        #点击登录
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.user_input))
        doc ="登录页面——登录功能"
        self.wait_eleVisible(loc.user_input,doc=doc)
        # self.driver.find_element(*loc.user_input).send_keys(username)
        # self.driver.find_element(*loc.passwd_input).send_keys(password)
        # self.driver.find_element(*loc.login_button).click()
        self.input_text(loc.user_input,username,doc=doc)
        self.input_text(loc.passwd_input, password, doc=doc)
        self.click_element(loc.login_button,doc=doc)


    def get_error_login(self):
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.login_error_info))
        doc = "登录页面-获取登录错误提示信息"
        self.wait_eleVisible(loc.login_error_info,doc=doc)
        # return self.driver.find_element(*loc.login_error_info).text
        return  self.get_text(loc.login_error_info,doc=doc)



    #
    # #获取错误提示信息   --登录区域
    # def get_errorMsg_from_loginArea(self):
    #     doc = "登录页面_获取登录区域错误提示"
    #     self.wait_eleVisible(loc.form_error_info,doc=doc)
    #     # WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='xxxxx']")))
    #     # return self.driver.find_element_by_xpath("//div[@class='xxxxx']").text
    #     return self.get_text(loc.form_error_info,doc)

    #获取错误信息  --页面正中间消失
    # def get_errorMsg_from_pageCenter(self):
    #     try:
    #         WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,"//a[@class='xxxxx']")))
    #         return True
    #     except:
    #         return False



    # #注册入口
    # def register_enter(self):
    #     # WebDriverWait(self.driver).until(EC.visibility_of_element_located((By.XPATH,"")))
    #     self.wait_eleVisible(loc)
    #     self.driver.find_element_by_xpath(" ").click()