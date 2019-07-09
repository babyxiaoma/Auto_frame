import os
import time
from selenium import webdriver
from utils.config import DRIVER_PATH,REPORT_PATH

#driver路径,可自行扩张
CHROMEDRIVER_PATH = DRIVER_PATH + '\\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\\IEDriverServer.exe'   #暂时不做其他浏览器,只用谷歌测试

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Edge}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH}

class UnSupportBrowserTypeError(Exception):
    pass

class Browser(object):
    def __init__(self,browser_type='chrome'):
        self._type = browser_type.lower()
        if browser_type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s' % ','.join(TYPES.keys()))
        self.driver = None

    def get(self,url,maximize_window=True,implicitly_wait=30):
        '''
        打开浏览器
        :param url:
        :param maximize_window: 窗口最大化
        :param implicitly_wait: 显示等待时间
        :return:
        '''
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)

    def save_screen_shot(self,name='screen_shot'):
        '''
        以当前时间为名字保存截图
        :param name: 截图name
        :return:
        '''
        day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\\screenshot_%s' % day
        #判断路径不在内存路径中,则创建路径
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S',time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' %(name,tm))
        return screenshot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()



if __name__ == '__main__':
    b = Browser(browser_type='chrome')
    b.get('http://ht.test.by-998.com')
    b.save_screen_shot('test_login2')
    time.sleep(2)
    b.quit()



