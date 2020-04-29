from selenium.webdriver.common.by import By

class LoginPageLocator:
    # 元素定位
    # 用户名输入框
    user_input = (By.XPATH, '//input[@id="txtUserName"]')
    # 密码输入框
    passwd_input = (By.XPATH, '//input[@id="txtPassword"]')
    # 登录按钮
    login_button = (By.XPATH, '//a[text()="登录"]')
    # 错误提示框
    login_error_info = (By.XPATH, "//div[@id='msg']/div/strong")


