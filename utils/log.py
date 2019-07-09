import logging
import datetime
from utils.config import LOG_PATH
from logging.handlers import TimedRotatingFileHandler
from utils.config import Config


class Logger(object):
    def __init__(self,logger_name='Auto_frame'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        #引入配置文件log
        c = Config().get('log')
        # 拼接使用当前时间为日志名
        log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        #日志文件名
        self.log_file_name = c.get('file_name') if c and c.get('file_name') else LOG_PATH + '\\' + log_file   #日志名
        self.backup_count = c.get('backup') if c and c.get('backup') else 5    #保留日志数量
        #日志输出级别
        self.console_output_level = c.get('console_level') if c and c.get('console_level') else 'WARNING'
        self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'
        #日志输出格式
        self.formatter = c.get('pattern') if c and c.get('pattern') else logging.Formatter('%(asctime)s -- %(name)s -- %(filename)s -- %(lineno)d -- %(levelname)s -- %(message)s')

    def get_logger(self):
        '''在logger添加日志句柄并返回,如果logger已有句柄,则直接返回'''
        if not self.logger.handlers:   #避免重复日志
            console_handler =logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            #每天重新创建一个日志,最多保留self.backup_count 份
            file_handler =  TimedRotatingFileHandler(filename=self.log_file_name,
                                                     when='D',
                                                     interval=1,
                                                     backupCount=self.backup_count,
                                                     delay=True,
                                                     encoding='utf-8'
                                                     )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger
#调用logger即可写入日志
logger =Logger().get_logger()



if __name__ == '__main__':
    log = Logger()
    print(log.logger.info('thi is a info!'))