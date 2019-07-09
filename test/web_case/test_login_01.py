import sys
sys.path.append(r'E:\Auto_frame')

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from utils.config import Config,DATA_PATH,REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from test.page.login_main_page import Loginmainpage

class TestLogin(unittest.TestCase):
    URL = Config().get('URL')
    excel_path = DATA_PATH + '\data.xls'


    def sub_setUp(self):
        self.driver = Loginmainpage()
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()


    def test_search(self):
        '''测试登录功能'''
        datas = ExcelReader(self.excel_path).data
        #参数化
        for i in datas:
            self.sub_setUp()
            self.driver.login(i['username'],i['password'])
            self.driver.wait()
            title = self.driver.title
            logger.info(title+'登录成功') if title in '首页' else logger.info('title不正确')
            self.sub_tearDown()

    def test_click_drop_page1(self):
        '''测试点击权限管理页面功能'''
        self.sub_setUp()
        self.driver.login('leon2017','passnew2017')
        self.driver.wait()
        self.driver.click_drop_page1()
        self.driver.wait()
        logger.info('点击权限管理页面成功-')
        self.sub_tearDown()

    def test_click_drop_page2(self):
        '''测试点击用户体系页面功能'''
        self.sub_setUp()
        self.driver.login('leon2017','passnew2017')
        self.driver.wait()
        self.driver.click_drop_page2()
        self.driver.wait()
        logger.info('点击用户体系页面成功-')
        self.sub_tearDown()



# if __name__ == '__main__':
#
#     report_path = REPORT_PATH + '\\report.html'
#     with open(report_path,'wb') as f:
#         runner = HTMLTestRunner(stream=f,verbosity=2,title='web测试用例',description='修改html测试报告')
#         runner.run(TestLogin('test_search'))
#     e = Email(server='smtp.qq.com',
#               sender='2538778461@qq.com',
#               password='efvczhscfbhzdjia',
#               receiver='aa2538778461@163.com',
#               title='web自动化测试报告',
#               path=report_path)
#     e.send()

