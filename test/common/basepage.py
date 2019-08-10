# -*- coding:utf-8 -*-
# @Time   : 2019-07-24 13:52
# @Author : xiao hei ma

import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from config.config import REPORT_PATH
from config.config import Config
from utils.log import Logger


# #driver路径,可自行扩张
# CHROMEDRIVER_PATH = DRIVER_PATH + '\\chromedriver.exe'
# IEDRIVER_PATH = DRIVER_PATH + '\\IEDriverServer.exe'   #暂时不做其他浏览器,只用谷歌测试


class BasePage(unittest.TestCase):
    """
      定义一个页面基类，让所有的页面都继承该类，封装一些常用的页面操作方法
      """
    logeer = Logger()
    config = Config()


    def setUp(self):
        self.logeer.logger.info('------------开始执行用例--------------')


    @classmethod
    def setUpClass(cls,browser_type='chrome',maximize_window=True,implicitly_wait=30):
        '''
        打开浏览器
        :param browser_type:浏览器类型
        :param maximize_window: 窗口最大化
        :param implicitly_wait: 显示等待时间默认30秒
        :return:
        '''
        cls._type = browser_type.lower()
        if cls._type == 'firefox':
            cls.driver = webdriver.Firefox()
        elif cls._type == 'chrome':
            cls.driver = webdriver.Chrome()
        elif cls._type == 'ie':
            cls.driver = webdriver.Edge()
        else:
            cls.logeer.logger.warning('仅支持火狐,谷歌,ie浏览器.....')
            pass
        #获取环境url
        cls.driver.get(cls.config.get('test')['url'])
        if maximize_window:
            cls.driver.maximize_window()
        cls.driver.implicitly_wait(implicitly_wait)



    def save_screen_shot(self,name='screen_shot'):
        '''
        以当前时间为名字保存截图
        :param name: 截图name
        :return:
        '''
        day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\\screenshot_%s' % day
        #判断路径不在内存路径中,则创建路径
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        tm = time.strftime('%H%M%S',time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' %(name,tm))
        return screenshot


    def find_element(self,loc):
        '''重写查找元素方法'''
        try:
            WebDriverWait(self.driver,15).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            self.logeer.logger.error('%s 页面中未能找到%s 元素' % (self, loc))


    def clear_key(self,loc):
        '''清空输入框'''
        time.sleep(3)
        self.find_element(loc).clear()

    def send_keys(self, loc, value):
        """输入内容"""
        self.clear_key(loc)
        self.find_element(loc).send_keys(value)

    def click_button(self, loc):
        """点击按钮"""
        self.find_element(loc).click()

    def close(self):
        '''关闭页面'''
        self.driver.close()

    def quit(self):
        '''关闭浏览器'''
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()



