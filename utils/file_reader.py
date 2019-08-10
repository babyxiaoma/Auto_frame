# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 读取配置文件类
# @File    : file_reader.py
# @Software: PyCharm

import yaml
import os
import xlrd


class YamlReader(object):
    '''读取yaml文件内容,返回list'''
    def __init__(self,yaml):
        if os.path.exists(yaml):
            self.yaml = yaml
        else:
            raise FileExistsError('文件不存在!')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yaml,'rb') as f:
                self._data = list(yaml.safe_load_all(f))   #组成一个list
        return self._data


class SheetTypeError(Exception):
    '''自定义一个异常类,接收传入sheettype异常'''
    pass
    

class ExcelReader(object):
    """
    读取excel文件中的内容。返回list。

    如：
    excel中内容为：
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |

    如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """
    def __init__(self,excel,sheet=0,title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileExistsError('文件不存在!')
        self.sheet = sheet
        self.title_line = title_line
        self._data = []

    @property
    def data(self):
        #判断没有self._data执行,否则直接返回self._data
        if not self._data:
            workbook = xlrd.open_workbook(self.excel)
            #判断self.sheet类型是否为int or str
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('请输入<type:int>或者<type:str>'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            #如果self.title_line为True,则组成dict,否则组成list
            if self.title_line:
                keys = s.row_values(0)  #首行为title
                for col in range(1,s.nrows):
                    #依次遍历其余行,与首行组成dict,拼到self._data中
                    values = s.row_values(col)
                    self._data.append(dict(zip(keys,values)))
            else:
                for col in range(0,s.nrows):
                    self._data.append(s.row_values(col))
        return self._data




if __name__ == '__main__':
    # y = YamlReader('E:\Auto_frame\config\config.yml')
    # print(y.data)

    from config.config import DATA_PATH
    x = ExcelReader(DATA_PATH + '\\api.xls')
    # x = ExcelReader('E:\Auto_frame\data\data.xls', title_line=False)
    print(x.data)