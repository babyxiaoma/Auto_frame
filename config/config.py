# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 初始化配置类
# @File    : config.py
# @Software: PyCharm

import os
from utils.file_reader import YamlReader
import datetime


class Read_Config(object):
    def __init__(self,config):
        self.config = YamlReader(config).data

    def get(self,element,index=0):
        '''
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        '''
        return self.config[index].get(element)


class config(object):
    def __init__(self):
        '''初始化配置'''
        # 初始化路径,通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
        self.BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        self.CONFIG_PATH = os.path.join(self.BASE_PATH, 'config', 'config.yml')
        self.DATA_PATH = os.path.join(self.BASE_PATH, 'data')
        self.DRIVER_PATH = os.path.join(self.BASE_PATH, 'drivers')
        self.LOG_PATH = os.path.join(self.BASE_PATH, 'log')
        self.API_REPORT_PATH = os.path.join(self.BASE_PATH, 'report','api_report.html')
        self.WEBCASE_PATH = os.path.join(self.BASE_PATH, 'test' + '\\web_case')
        self.APICASE_PATH = os.path.join(self.BASE_PATH, 'test' + '\\api_case')

        self.c = Read_Config(config=self.CONFIG_PATH)
        # 拼接使用当前时间为日志名
        self.log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        self.log_file_name = self.LOG_PATH + '\\' + self.log_file

        self.API_URL = self.c.get('API_URL')
        self.username = self.c.get('username')
        self.password = self.c.get('password')
        self.file_name = self.c.get('log')['file_name']
        self.backup = self.c.get('log')['backup']
        self.console_level = self.c.get('log')['console_level']
        self.file_level = self.c.get('log')['file_level']
        self.pattern = self.c.get('log')['pattern']
        self.host = self.c.get('db')['host']
        self.port = self.c.get('db')['port']
        self.user = self.c.get('db')['user']
        self.passwd = self.c.get('db')['passwd']
        self.db = self.c.get('db')['db']






if __name__ == '__main__':
    c = config()
    # print(test.config)
    print(c.db)



