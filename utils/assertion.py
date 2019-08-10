# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 断言类
# @File    : assertion.py
# @Software: PyCharm



from utils.reader_db import Reader_Mysql

class Error(object):
    '''
        各种断言方法写在此处
    '''
    def assertHTTPCode(self,response,code_list=None):
        '''
        针对公司项目接口返回的code获取
        :param response: 传入response必须为json
        :param code_list:响应code_list,默认不传为0
        :return:
        '''
        res_code = response['code']
        if not code_list:
            code_list = [0]
        if res_code not in code_list:
            raise AssertionError('响应code值不在列表中!,实际响应code:%s,实际响应:%s' % (res_code,response))


    def assertMysqldata(self,sql:str,expect_data:str):
        '''
        对比sql结果和预期结果
        :param sql: sql语句
        :param expect_data: 预期结果
        :return:
        '''
        te = Reader_Mysql()
        sql_data = te.get_sql_data(sql)
        if sql_data != expect_data:
            raise ValueError('数据库查询数据与预期结果不一致!数据库结果:%s,预期结果:%s' % (sql_data,expect_data))

