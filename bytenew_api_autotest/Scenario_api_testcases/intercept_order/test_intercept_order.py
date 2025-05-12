from datetime import datetime, timedelta
#import datetime
import json
import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt
from Base.Get_token_pre import Get_token
#from Base.Get_token_test.Get_admin_token import Get_token
from common.Get_time import Get_time
from Base.Get_xxjob_token import Get_token as Get_xxjob_token
from config import config

'''
杭州云贝-【抖音】紫貂的小店的拦退单拉取
'''
@ddt.ddt
class MyTestCase(unittest.TestCase):
    cases = common.Common().ReadExcelTypeDict("lg_admin_update_dy.xlsx")
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.logs.info("========= 测试开始 =========")
        cls.admin_token = Get_token.lg_artifact_admin_pre_token()
        cls.logs.info(f"cookie获取结果: {cls.admin_token}")
        cls.xxjob_pre_token = Get_xxjob_token.lg_xxjob_pre_token()
        cls.logs.info(f"cookie获取结果: {cls.xxjob_pre_token}")
    @ddt.data(*cases)
    def test_lg_admin_updatePullTime_dy_refundApply(self,pars):
        '''
        修改杭州云贝-【抖音】紫貂的小店 的售后单拉取时间
        '''
        # 动态显示用例名称（从Excel读取）
        case_name = pars.get('casename')
        self.logs.info(f"▶▶▶ 执行操作: {case_name} ◀◀◀")
        #self.logs.debug(f"测试数据明细: {pars}")

        url = pars['url']
        headers = {'Content-Type': 'application/json',"token":self.admin_token }
        method = pars['请求方式']
        datas = json.loads(pars['body']) if isinstance(pars['body'], str) else pars['body'].copy()
        # 获取当前时间并减 1 分钟
        datas['beginTime'] = Get_time.before_now(self)
        # 获取当前时间
        datas['endTime'] = Get_time.now(self)
        body = json.dumps(datas)
        expected_res = pars['预期结果']

        result = Base().requests_type(method=method, url=url, headers=headers,data=body)
        self.logs.info(f"响应数据：{result.json()}")

        self.assertEqual(result.json()['success'], expected_res, "接口返回结果不符合预期")

    def test_xxjob_dy_refundApply(self):
        '''
            执行 抖音店铺 的售后单拉取定时任务
        '''
        self.logs.info(f"▶▶▶ 执行操作: 执行 抖音店铺 的售后单拉取定时任务 ◀◀◀")
        url = config.xxjob_host + "/jobinfo/trigger"
        header = {'Content-Type': 'application/x-www-form-urlencoded', "Cookie": self.xxjob_pre_token}
        method = 'POST'
        datas = {"id": "355", "executorParam": "", "addressList": ""}
        result = Base().requests_type(method=method, url=url, headers=header, data=datas)
        self.logs.info(f"响应结果：{result.text}")

        self.assertEqual(result.status_code, 200, "接口执行失败")

if __name__ == '__main__':
    unittest.main()
