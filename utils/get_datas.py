# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 获取token数据类
# @File    : get_datas.py
# @Software: PyCharm

from config.config import config
from utils.client import HTTPClient


class GETTOKENException(Exception):
    '''接收当获取token时出现异常抛出错误'''
    pass

class GetData(object):
    def __init__(self):
        self.c = config()
        self.API_URL = self.c.API_URL
        self.token = self.get_token()  #获取token为全局变量

    def get_token(self):
        '''获取登录接口api_token字典'''
        url =  self.API_URL + 'pub/login'
        data = {
            'username':self.c.username,
            'password':self.c.password
        }
        try:
            res = HTTPClient(url=url,method='post').send(data=data)
        except Exception as e:
            raise GETTOKENException('获取登录响应失败: %s' % str(e))
        token = res.json()['data']
        data_dict = {'api_token':token}
        return data_dict

    @property
    def get_activity_gold_id(self):
        '''体验金id'''
        url = self.API_URL + 'activity/activity_gold_id'
        res = HTTPClient(url=url,method='get').send(params=self.token).json()
        try:
            dict_id = {'id':res['data']['id']}
            datas = dict(self.token,**dict_id)    #合并两个字典为一个字典
            return datas
        except Exception:
            pass
            # raise ValueError('获取体验金id错误,请检查返回响应!返回响应为:%s' % res)

    @property
    def get_activity_index(self):
        '''救援活动id'''
        url = self.API_URL + 'activity/index'
        res = HTTPClient(url=url,method='get').send(params=self.token).json()
        try:
            dict_id = {'id':res['data'][1]['id'],'rule_id':res['data'][1]['rule'][0]['id']}
            datas = dict(self.token, **dict_id)
            return datas
        except Exception:
            pass
            # raise ValueError('获取救援活动id错误,请检查返回响应!返回响应为:%s' % res)

    @property
    def get_activity_get_status_sign(self):
        '''签到活动id'''
        url = self.API_URL + 'activity/get_status_sign'
        res = HTTPClient(url=url, method='get').send(params=self.token).json()
        try:
            Activity_id = {'id':res['data'][0]['Activity_id']}
            datas = dict(self.token, **Activity_id)
            return datas
        except Exception:
            pass
            # raise ValueError('获取签到id错误,请检查返回响应!返回响应为:%s' % res)

    @property
    def get_activity_lucky(self):
        '''黄金转盘活动id'''
        url = self.API_URL + 'activity/index'
        res = HTTPClient(url=url, method='get').send(params=self.token).json()
        try:
            for i in res['data']:
                if i['activity_name'] == '黄金轮盘':
                    id = i['id']
            dict_id = {'id':id}
            datas = dict(self.token, **dict_id)
            return datas
        except Exception:
            pass
            # raise ValueError('获取转盘活动id错误,请检查返回响应!返回响应为:%s' % res)

    @property
    def get_platform_games_KY(self)->dict:
        '''KY游戏id(三公)'''
        url = self.API_URL + 'platform/games'
        res = HTTPClient(url=url, method='get').send().json()
        try:
            for i in res['data']['AGIN']:
                if i['plat_code'] == 'KY':
                    code = i['code']
                    break
            dict_id = {'platform_played_id': code,'platform_type':'KY'}
            datas = dict(self.token, **dict_id)
            return datas
        except Exception:
            pass
            # raise ValueError('获取KY游戏id错误,请检查返回响应!返回响应为:%s' % res)

    @property
    def get_platform_games_AGIN(self):
        '''AGIN游戏id(捕鱼达人)'''
        dict_id = {'platform_played_id': 6, 'platform_type': 'AGIN'}
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_platform_games_BBIN(self):
        '''BBIN游戏id(糖果派对2)'''
        dict_id = {'platform_played_id': 5908, 'platform_type': 'BBIN'}
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_platform_transfer_KY(self):
        '''KY游戏转出'''
        dict_id = {'type':'OUT', 'platform_type': 'KY'}
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_platform_transfer_AGIN(self):
        '''AGIN游戏转出'''
        dict_id = {'type': 'OUT', 'platform_type': 'AGIN'}
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_platform_transfer_BBIN(self):
        '''BBIN游戏转出'''
        dict_id = {'type': 'OUT', 'platform_type': 'BBIN'}
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_yeb_transfer_in(self):
        '''余额宝转入金额1'''
        dict_id = {'amount':1}        #余额宝转入金额写死1
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_yeb_transfer_out(self):
        '''余额宝转出金额1'''
        dict_id = {'amount': 1,'passwd':123456}   #交易密码写死,无接口获取,根据账号修改
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_user_alipay(self):
        '''编辑支付宝信息'''
        dict_id = {'alipay_username': '小黑', 'alipay_account': 88889999}  # 编辑支付宝信息写死
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_pay_transfer(self):
        '''编辑公司入款提交信息'''
        dict_id = {'bank_username': '黄河老祖', 'bank_account': 50421541056616544,'bank_name':'工商银行','gath_username':'王大佬','amount':10,'type':'公司'}  # 编辑公司入款提交信息写死
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_user_setNickname(self):
        '''编辑设置昵称信息'''
        dict_id = {'nickname': 'My哒哒哒奖金'}  # 编辑设置昵称信息写死
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_user_withdraw(self):
        '''编辑申请提款信息'''
        dict_id = {'amount':50,'withdraw_type':0,'withdraw_account':50}  # 编辑申请提款信息写死
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_activity_id(self):
        '''转盘活动id,无token'''
        return  {"id":40}

    @property
    def get_user_save_coinpassword(self):
        '''编辑取款密码信息'''
        dict_id = {'oldcoinPassword': '', 'coinPassword':111111, 'confirmcoinPassword':111111}  # 编辑取款密码信息写死
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_amend_user_save_coinpassword(self):
        '''修改取款密码信息'''
        dict_id = {'oldcoinPassword':111111, 'coinPassword': 123456, 'confirmcoinPassword': 123456}  # 编辑取款密码信息写死
        datas = dict(self.token, **dict_id)
        return datas

    @property
    def get_user_balance(self):
        '''获取用户余额coin字段'''
        url = self.API_URL + 'user/balance'
        res = HTTPClient(url=url,method='get').send(params=self.token).json()
        coin = res['data']['coin']
        return coin





if __name__ == '__main__':
    t = GetData()
    print(t.token)
    print(t.get_activity_get_status_sign)


