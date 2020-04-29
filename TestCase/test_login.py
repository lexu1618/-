import unittest
from  selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas.login_datas import LoginDatas as LD
from TestDatas import Common_Datas as CD
import ddt
import pytest

@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
@pytest.mark.demo
def test_demo():
    demo()
    assert False

def demo():
    print("**************")
    print("1222222222222")



@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:     #测试用例 = 测试对象调用+测试数据
                                        #注意用例的独立性
    # @classmethod
    # def setUpClass(cls):
    #     # 前置  访问登录界面
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(CD.web_login_url)
    #     cls.lg = LoginPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     # 后置   关闭浏览器
    #     cls.driver.quit()
    #
    # def setUp(self):
    #     pass
    #
    # def tearDown(self):
    #     self.driver.refresh()



    #异常用例
    @pytest.mark.parametrize("data",LD.wrong_data)
    def test_login_0_wrong_data(self,data,access_web):

        access_web[1].login(data["user"],data["password"])

        #断言
        assert access_web[1].get_error_login()== data["check"]

    @pytest.mark.parametrize("caseData",LD.errorPwd_noReg)
    def test_login_1_noReg(self,caseData,access_web):
        access_web[1].login(caseData["user"],caseData["password"])
        assert access_web[1].get_error_login() ==caseData["check"]


    #正常登录用例
    @pytest.mark.smoke
    def test_login_2_success(self,access_web):
        #步骤   输入用户名 密码 点击登录
        access_web[1].login(LD.success_data["user"],LD.success_data["password"])

        #断言
        assert IndexPage(access_web[0]).isExist_login_ele()