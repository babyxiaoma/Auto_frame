import requests
from utils.log import logger

#接口方法
METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']

class UnSupportMethodException(Exception):
    """当传入的method的参数不是支持的类型时抛出此异常。"""
    pass

class HTTPClient(object):
    def __init__(self,url,method='GET',headers=None,cookies=None):
        self.url = url
        self.headers = headers
        self.cookies = cookies
        self.session = requests.session()
        self.method = method.upper()
        if self.method not in METHODS:
            raise UnSupportMethodException('不支持method:{0},请检查传参!'.format(self.method))

        self.set_headers()
        self.set_cookies()

    def set_headers(self):
        '''有headers时更新headers'''
        if self.headers:
            self.session.headers.update(self.headers)

    def set_cookies(self):
        '''有cookies时更新cookies'''
        if self.cookies:
            self.session.cookies.update(self.cookies)


    def send(self, params=None, data=None, **kwargs):
        response = self.session.request(url=self.url,method=self.method, params=params, data=data, **kwargs)
        response.encoding = 'utf-8'
        logger.info('{0} {1}'.format(self.method, self.url))
        logger.info('请求成功: {0}'.format(response.text))
        return response



if __name__ == '__main__':

    url = 'http://api.test.by-998.com/user/balance'
    data = {'api_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjI2NDM1NzAsImV4cCI6MTU2MjY4Njc3MCwiaXNzIjoiYm9uZyIsInN1YiI6ODM4OH0.sEbrbx_9E5mzuPYSGhoZzHcNPugy457kn2MDGt8EViQ'}

    # print(url,data)
    h = HTTPClient(url=url,method='get').send(params=data).json()
    # for i in h['data']:
    #     if i['activity_name'] == '黄金轮盘':
    #         print(i['id'])
    coin = h['data']['coin']
    print(coin,type(coin))