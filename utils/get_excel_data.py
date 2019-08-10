# -*- coding: utf-8 -*-

# @Time    : 2019/8/8 14:02
# @Author  : xiao hei ma
# @Desc    : 获取api_data类
# @File    : get_execle_data.py
# @Software: PyCharm

from utils.get_datas import GetData


class Excel_Data(object):
    def __init__(self):
        self.data = GetData()
        self._data = self.excel_data()

    def excel_data(self):
        '''根据传入key值获取dict数据信息作为data'''
        datas = {
            'api_token':self.data.token,
            '体验金id':self.data.get_activity_gold_id,
            '救援活动id':self.data.get_activity_index,
            '签到活动id':self.data.get_activity_get_status_sign,
            '黄金转盘活动id':self.data.get_activity_lucky,
            'KY_id':self.data.get_platform_games_KY,
            'KY_OUT':self.data.get_platform_transfer_KY,
            'AGIN_id':self.data.get_platform_games_AGIN,
            'AGIN_OUT':self.data.get_platform_transfer_AGIN,
            'BBIN_id':self.data.get_platform_games_BBIN,
            'BBIN_OUT':self.data.get_platform_transfer_BBIN,
            '余额宝转入1':self.data.get_yeb_transfer_in,
            '余额宝转出1':self.data.get_yeb_transfer_out,
            '支付宝信息':self.data.get_user_alipay,
            '公司入款信息':self.data.get_pay_transfer,
            '用户昵称':self.data.get_user_setNickname,
            '提款信息':self.data.get_user_withdraw,
            '活动id':self.data.get_activity_id,
            '编辑取款密码':self.data.get_user_save_coinpassword,
            '修改取款密码':self.data.get_amend_user_save_coinpassword
        }
        return datas

    def get_coin(self):
        '''获取余额coin'''
        return self.data.get_user_balance




if __name__ == '__main__':
    d = Excel_Data()
    # print(d.excel_data()['api_token'])
    print(d.get_coin(),type(d.get_coin()))
    # print(d['体验金id'])

