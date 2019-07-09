from test.common.page import Page
from selenium.webdriver.common.by import By
import time
class Loginmainpage(Page):
    #登录功能
    locator_username = (By.NAME, 'username')
    locator_password = (By.NAME, 'password')
    locator_button = (By.ID, 'login')
    #点击下拉框页面功能
    # 权限管理
    locator_click0 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[2]/a')
    #用户列表
    locator_page0 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[2]/ul/li[1]/a')
    #角色列表
    locator_page1 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[2]/ul/li[2]/a')
    #权限列表
    locator_page2 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[2]/ul/li[3]/a')

    # 用户体系
    locator_click1 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[3]/a')
    locator_page3 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[3]/ul/li[1]/a')
    locator_page4 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[3]/ul/li[2]/a')
    locator_page5 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[3]/ul/li[3]/a')
    locator_page6 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[3]/ul/li[4]/a')
    locator_page7 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[3]/ul/li[5]/a')
    locator_page8 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[3]/ul/li[6]/a')
    locator_page9 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[3]/ul/li[7]/a')



    # 支付管理
    locator_click2 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[4]/a')
    # 活动管理
    locator_click3 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[5]/a')
    # 现金管理
    locator_click4 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[6]/a')
    # 报表
    locator_click5 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[7]/a')
    # 系统管理
    locator_click6 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[8]/a')
    # 平台管理
    locator_click7 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[9]/a')
    # 余额宝
    locator_click8 = (By.XPATH,'/html/body/div[1]/aside/section/ul/li[10]/a')



    def login(self,username,password):
        '''登录功能'''
        self.find_element(*self.locator_username).send_keys(username)
        self.find_element(*self.locator_password).send_keys(password)
        self.find_element(*self.locator_button).click()

    def click_drop_page1(self):
        '''点击权限管理页面功能'''
        self.find_element(*self.locator_click0).click()
        self.find_element(*self.locator_page0).click()
        self.find_element(*self.locator_page1).click()
        self.find_element(*self.locator_page2).click()

    def click_drop_page2(self):
        '''点击用户体系页面功能'''
        self.find_element(*self.locator_click1).click()
        self.find_element(*self.locator_page3).click()
        self.find_element(*self.locator_page4).click()
        self.find_element(*self.locator_page5).click()
        self.find_element(*self.locator_page6).click()
        self.find_element(*self.locator_page7).click()
        self.find_element(*self.locator_page8).click()
        self.find_element(*self.locator_page9).click()


