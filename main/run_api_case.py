# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 运行发送测试报告类
# @File    : run_api_case.py
# @Software: PyCharm

import sys
import os
sys.path.append(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])
from utils.HTMLTestRunner import HTMLTestRunner
import unittest
from config.config import config
from utils.mail import Email

def run(testname: str):
    '''
    运行测试用例生成html报告
    :param testname: 测试人
    :return:
    '''
    c = config()
    #获取测试账号转换为str
    test_username = str(c.username)

    with open(c.API_REPORT_PATH, 'wb') as f:
        suite = unittest.defaultTestLoader.discover(start_dir=c.APICASE_PATH, pattern='test_*.py')
        runner = HTMLTestRunner(stream=f,
                                verbosity=2,
                                title='API测试报告',
                                description='接口html测试报告',
                                tester=testname,
                                test_user=test_username)
        runner.run(suite)
    e = Email(server='smtp.qq.com',
              sender='2538778461@qq.com',
              password='efvczhscfbhzdjia',
              receiver='aa2538778461@163.com',
              title='老马发送的今天的API自动化报告又来了，请注意查看！',
              message='来了来了，你的测试API自动化报告!!，注意如果收不到邮件注意查看垃圾箱还是退信了！',
              path=[c.API_REPORT_PATH,c.log_file_name]
              )
    e.send()


# 运行
#传入测试人name
run(testname='xiao hei ma')
