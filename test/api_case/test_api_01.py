# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 主运行入口类
# @File    : test_api_01.py
# @Software: PyCharm

import sys
import os
sys.path.append(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])
import unittest
from config.config import config
from utils.client import HTTPClient
from utils.log import logger
from utils.assertion import Error
from utils.file_reader import ExcelReader
from utils.get_excel_data import Excel_Data
from utils.reader_db import Reader_Mysql


class Test_API(unittest.TestCase):
    c = config()
    e = Error()
    excel_path = c.DATA_PATH + '\\api.xls'
    excel_data = Excel_Data()
    reader_sql = Reader_Mysql()

    def test_api_all(self):
        '''测试接口'''
        datas = ExcelReader(self.excel_path).data
        for d in datas:
            if d['run'].lower() == 'yes':
                with self.subTest(data=d['describe']):
                    url = self.c.API_URL + d['api']
                    method = d['method']
                    data = d['data']
                    sql_value = d['sql_value']
                    expect_data = str(d['expect_data'])
                    pd_id = d['pd_id']
                    # 判断excel上面的data不为空时执行获取datas,否则执行不传data的get方法
                    if data != '':
                        datas = self.excel_data.excel_data()[data]
                        if method == 'post':
                            res = HTTPClient(url=url, method=method).send(data=datas).json()
                        else:
                            res = HTTPClient(url=url, method=method).send(params=datas).json()
                    else:
                        res = HTTPClient(url=url, method=method).send().json()

                    logger.debug('响应code字段:%s' % res['code'])
                    # 判断响应json数据中的code字段
                    self.e.assertHTTPCode(res)
                    #判断sql结果和预期结果
                    if sql_value:
                        if pd_id:
                            expect_data = self.excel_data.get_coin()   #替换预期结果为账号最新余额coin字段
                        sql = self.reader_sql.get_new_date_all_activity_id(sql_value)
                        self.e.assertMysqldata(sql,expect_data)




# if __name__ == '__main__':
# #     # unittest.main()
#     report_path = REPORT_PATH + '\\api_report.html'
#     with open(report_path,'wb') as f:
#         runner = HTMLTestRunner(stream=f,      #报告路径
#                                 verbosity=2,
#                                 title='API测试报告',   #报告标题
#                                 description='接口html测试报告',   #描述可不写
#                                 tester='小黑')   #测试人
#         runner.run(TestUserAPI('test_login_01'))     #添加用例类里面的用例方法
# #     发送邮件
#     e = Email(server='smtp.qq.com',
#                   sender='2538778461@qq.com',
#                   password='efvczhscfbhzdjia',
#                   receiver='aa2538778461@163.com',
#                   title='API自动化测试报告',
#                   path=report_path)
#     e.send()
