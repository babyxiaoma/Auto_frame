import sys
sys.path.append(r'E:\Auto_frame')
from utils.HTMLTestRunner import HTMLTestRunner
import unittest
from utils.config import WEBCASE_PATH,REPORT_PATH
from utils.mail import Email

def run(testname):
    '''运行测试用例生成html报告'''
    report_path = REPORT_PATH + '\\web_report.html'
    with open(report_path, 'wb') as f:
        suite = unittest.defaultTestLoader.discover(start_dir=WEBCASE_PATH, pattern='test_*.py')
        runner = HTMLTestRunner(stream=f,
                                verbosity=2,
                                title='web自动化测试报告',
                                description='UIhtml测试报告',
                                tester=testname)
        runner.run(suite)
    # e = Email(server='smtp.qq.com',
    #           sender='2538778461@qq.com',
    #           password='efvczhscfbhzdjia',
    #           receiver='aa2538778461@163.com',
    #           title='web自动化测试报告',
    #           message='测试后台web自动化测试报告!!',
    #           path=report_path
    #           )
    # e.send()

#运行
run(testname='xiao hei ma')
