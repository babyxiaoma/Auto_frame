import os
from utils.file_reader import YamlReader


# 初始化路径,通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH = os.path.join(BASE_PATH,'config','config.yml')
DATA_PATH = os.path.join(BASE_PATH,'data')
DRIVER_PATH = os.path.join(BASE_PATH,'drivers')
LOG_PATH = os.path.join(BASE_PATH,'log')
REPORT_PATH = os.path.join(BASE_PATH,'report')
WEBCASE_PATH = os.path.join(BASE_PATH,'test'+'\\web_case')
APICASE_PATH = os.path.join(BASE_PATH,'test'+'\\api_case')





class Config(object):
    def __init__(self,config=CONFIG_PATH):
        self.config = YamlReader(config).data

    def get(self,element,index=0):
        '''
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        '''
        return self.config[index].get(element)

if __name__ == '__main__':
    test = Config()
    # print(test.config)
    print(test.get('username'))



