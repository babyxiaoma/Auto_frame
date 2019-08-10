# -*- coding:utf-8 -*-
# @Time   : 2019-07-24 13:52
# @Author : xiao hei ma


from config.config import Config
from test.common.basepage import BasePage

PAGE_PATH =r'E:\python\python基础\Auto_frame\config\page_element.yaml'


class Log(BasePage):
    '''操作层'''
    #登录页面
    login_elements = Config(config=PAGE_PATH)
    close_button = ('xpath',login_elements.get('close_button'))
    username_loc = ('xpath',login_elements.get('username_loc'))
    password_loc = ('xpath',login_elements.get('password_loc'))
    code_loc = ('xpath',login_elements.get('code_loc'))
    login_loc = ('xpath',login_elements.get('login_loc'))
    registered_loc = ('xpath',login_elements.get('registered_loc'))

    def switch_to_frame(self,value):
        '''进入iframe页面'''
        self.driver.switch_to.frame(value)

    def click_close_button(self):
        '''点击弹窗公告关闭按钮'''
        self.click_button(self.close_button)

    def input_username(self,username):
        '''输入用户名'''
        self.send_keys(self.username_loc,username)

    def input_password(self,password):
        '''输入密码'''
        self.send_keys(self.password_loc,password)

    def input_code(self,code):
        '''输入验证码'''
        self.send_keys(self.code_loc,code)

    def click_login_button(self):
        '''点击登录按钮'''
        self.click_button(self.login_loc)

    def click_registered_button(self):
        '''点击注册按钮'''
        self.click_button(self.registered_loc)





