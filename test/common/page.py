from test.common.browser import Browser
import time

class Page(Browser):
    def __init__(self,page=None,browser_type='chrome'):
        if page:
            self.driver = page.driver
        else:
            super(Page,self).__init__(browser_type=browser_type)

    def get_driver(self):
        '''获取driver'''
        return self.driver

    @property
    def current_window(self):
        '''获取当前页面句柄'''
        return self.driver.current_window_handle

    @property
    def current_url(self):
        '''获取当前页面的url'''
        return self.driver.current_url

    @property
    def title(self):
        '''获取title'''
        return self.driver.title

    def find_element(self,*args):
        '''获取element'''
        return self.driver.find_element(*args)

    def find_elements(self,*args):
        '''获取elements'''
        return self.driver.find_elements(*args)

    def wait(self,seconds=3):
        '''强制等待,默认不传为3秒'''
        time.sleep(seconds)

