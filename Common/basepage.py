#封装基本函数   --执行日志   异常处理   失败截图
#所有页面的公共部分

import logging
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from Common.dir_config import *

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    #等待元素可见
    def wait_eleVisible(self,locator, timeout=20, poll_frequency=0.5,doc = ''):
        '''

        :param locator: 元素定位，元祖形式（定位类型，定位方式）
        :param timeout:
        :param poll_frequency:
        :param doc: 模块名_页面名称_操作名称
        :return:
        '''
        logging.info("等待元素{0}可见".format(locator))
        try:
            #开始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end-start).seconds
            logging.info("{0}：元素{1}可见，等待起始时间：{2}，等待结束时间{3}，等待时长：{4}".format(doc,locator,start,end,wait_time))
        except:
            logging.exception("{0} 秒内页面{1}中存在元素：{2}".format(timeout,doc,locator))
            #截图
            self.save_screenshot(doc)
            raise

    #等待元素存在
    def wait_elePresence(self,locator,timeout = 20,doc=''):
        logging.info("等待元素{0}可见".format(locator))
        try:
            #开始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end-start).seconds
            logging.info("{0}：元素{1}可见，等待起始时间：{2}，等待结束时间{3}，等待时长：{4}".format(doc,locator,start,end,wait_time))
        except:
            logging.exception("{0} 秒内页面{1}中存在元素：{2}".format(timeout,doc,locator))
            #截图
            self.save_screenshot(doc)
            raise

    #查找元素
    def get_element(self,locator,doc=''):
        logging.info("查找元素{}".format(locator))

        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！！！！！")
            self.save_screenshot(doc)
            raise

    #点击操作
    def click_element(self,locator,doc=''):
        #找元素
        ele = self.get_element(locator,doc)
        #元素操作
        logging.info("{0}:点击元素：{1}".format(doc,locator))

        try:
            ele.click()
        except:
            logging.exception("元素点击失败")
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_text(self,locator,text,doc=''):
        #找元素
        ele = self.get_element(locator,doc)
        #输入操作
        logging.info("{0} 输入元素：{1}".format(doc,locator))
        try:
            ele.send_keys(text)
        except:
            logging.info("元素输入失败！！！！！")
            self.save_screenshot(doc)
            raise


    #获取元素文本内容
    def get_text(self,locator,doc):
        #找元素
        ele = self.get_element(locator,doc)
        logging.info("{0} 获取元素文本：{1}".format(doc,locator))
        try:
            return  ele.text
        except:
            logging.exception("获取元素文本失败！！！！！")
            self.save_screenshot(doc)
            raise





    #获取元素属性


    #alert处理


    #上传操作


    #滚动条处理


    #窗口切换

    #iframe切换



    def save_screenshot(self,name):
        #图片名称： 模块名_页面名称_操作名称_时间.png
        now = time.strftime("%Y-%m-%d  %H-%M-%S")
        file_name = screenshot_dir + name +now +".png"
        try:
            self.driver.save_screenshot(file_name)
            logging.info("截图成功，文件路径为{}".format(file_name))
        except:
            logging.exception("截图失败")
