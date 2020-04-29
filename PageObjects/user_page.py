from Common.basepage import BasePage
from PageLocators.userpage_locator import UserPageLocators as loc

class UserPage(BasePage):
    #获取用户余额
    def get_user_leftMoney(self):
        doc = "个人页面_获取用户余额"
        #等待元素
        self.wait_eleVisible(loc.user_leftMoney,doc=doc)
        #获取个人可用余额
        text = self.get_text(loc.user_leftMoney,doc)
        #截取数字部分  --分隔符为元
        return text.strip("元")