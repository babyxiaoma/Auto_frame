'''抽取器,从响应结果中抽取部分数据'''
import json
import jmespath


class JMESPathExtractor(object):
    '''
    用JMESPath实现的抽取器，对于json格式数据实现简单方式的抽取
    '''
    def extract(self,query=None,body=None):
        try:
            return jmespath.search(expression=query,data=json.loads(body))
        except Exception as e:
            raise ValueError('无效查询:' + query + ':' +str(e))

if __name__ == '__main__':
    from utils.client import HTTPClient
    url = 'http://api.test.by-998.com/pub/login'
    data = {
        'username': '12133446101',
        'password': '123456'
    }
    res = HTTPClient('http://api.test.by-998.com/pub/login','post').send(data=data).text
    print(res)


    j = JMESPathExtractor()
    msg = j.extract('msg',res)
    data = j.extract('data',res)
    print(msg,data)
    '''
    操作成功
    eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjIxMzk4OTgsImV4cCI6MTU2MjE4MzA5OCwiaXNzIjoiYm9uZyIsInN1YiI6ODI1Nn0.V8grJNmNhRjmBkwW_v - LnT2MoVTstz98rQ - cbfDKjn4
    '''