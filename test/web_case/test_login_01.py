import sys
sys.path.append(r'E:\Auto_frame')

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from utils.log import Logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from test.page.Login_handle import Log

class TestLogin(Log,unittest.TestCase):
    logeer = Logger().logger

    def test_01(self):
        '''登录'''
        self.click_close_button()
        time.sleep(2)
        self.input_username('test0611')
        self.input_password('123456')
        self.input_code('8888')
        self.click_login_button()
        self.logeer.debug('登录!')




if __name__ == '__main__':
    unittest.main()
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

