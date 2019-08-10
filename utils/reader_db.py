# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 查询数据库类
# @File    : reader_db.py
# @Software: PyCharm

import pymysql
from config.config import config
import time
from decimal import *

class Reader_Mysql(object):
    def __init__(self):
        '''数据库配置'''
        self.c = config()
        self.host = self.c.host
        self.port = self.c.port
        self.user = self.c.user
        self.passwd = self.c.passwd
        self.db = self.c.db

    def get_sql_data(self,sql):
        '''
        获取查询数据的字段
        :param sql: 查询的sql
        :return:
        '''
        try:
            db = pymysql.connect(
                host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db
            )
            cursor = db.cursor()
            cursor.execute(sql)
            datas = cursor.fetchone()
            cursor.close()
            #判断类型不是str,int就为Decimal,转换Decimal为str保留4位小数
            if type(datas[0]) not in [str,int]:
                return str(Decimal(datas[0]).quantize(Decimal('0.0000')))
            #判断不是str,都强转为str
            elif type(datas[0]) not in [str]:
                return str(datas[0])
            else:
                return datas[0]
        except Exception:
            pass



    def get_new_date_all_activity_id(self,sql_value):
        '''
        根据传入的方法和字段数据返回出sql
        :param sql_value: excel上获取的value
        :return:
        '''
        #格式化当前时间
        self.time = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))

        id_name = sql_value.split('>')[0]
        field = sql_value.split('>')[1]
        id_value = sql_value.split('>')[2]
        if id_name == 'user_info':
            return "select %s from gygy_members WHERE username = '%s'" % (field,self.c.username)
        elif id_name == 'activity':
            return "select %s from gygy_activity_apply WHERE apply_date = '%s' and activity_id = %s" % (field,self.time,id_value)
        else:
            return None



if __name__ == '__main__':
    t = Reader_Mysql()
    sql = t.get_new_date_all_activity_id('user_info>username>')
    print(sql)
    a = t.get_sql_data(sql)
    print(a)
    print(type(a))







