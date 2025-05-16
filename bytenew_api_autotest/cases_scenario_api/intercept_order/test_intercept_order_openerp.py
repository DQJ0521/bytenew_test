#import datetime
import json
import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt
from Base.Get_token import Get_token
#from Base.Base_test.Get_admin_token import Get_token
from common.Get_time import Get_time
from Base.Get_xxjob_token import Get_token as Get_xxjob_token
from cases_api.xxjob.xxjob_tigger import xxjob_tigger
import config.config as config

@ddt.ddt
class MyTestCase(unittest.TestCase):
    '''
    开启erp的公司（杭州云贝-班牛）的拦截模拟：
    '''
    cases = common.Common().ReadExcelTypeDict_sliced(file_name="lg_admin_update_cases.xlsx",start_row=2,end_row=3)
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.logs.info("========= 测试开始 =========")
        cls.admin_token = Get_token.lg_artifact_admin_token()
        #cls.logs.info(f"cookie获取结果: {cls.admin_token}")
        cls.xxjob_pre_token = Get_xxjob_token.lg_xxjob_pre_token()
        #cls.logs.info(f"cookie获取结果: {cls.xxjob_pre_token}")
    @ddt.data(*cases)
    def test_lg_admin_updatePullTime_dy_refundApply(self,pars):
        '''
        修改三青小小号-【抖音】XXX 的售后单拉取时间
        '''
        # 动态显示用例名称（从Excel读取）
        case_name = pars.get('casename')
        self.logs.info(f"▶▶▶ 执行操作: {case_name} ◀◀◀")
        #self.logs.debug(f"测试数据明细: {pars}")

        url = config.admin_host+ pars['url']
        headers = {'Content-Type': 'application/json',"token":self.admin_token }
        method = pars['请求方式']
        datas = json.loads(pars['body']) if isinstance(pars['body'], str) else pars['body'].copy()
        # 获取当前时间并减 1 分钟
        #datas['beginTime'] = Get_time.before_now(self)
        datas['beginTime'] = "2025-05-16 14:32:13"
        # 获取当前时间
        #datas['endTime'] = Get_time.now(self)
        datas['endTime'] = "2025-05-16 14:32:13"
        body = json.dumps(datas)
        expected_res = pars['预期结果']

        result = Base().requests_type(method=method, url=url, headers=headers,data=body)
        self.logs.info(f"响应数据：{result.json()}")

        self.assertEqual(result.json()['success'], expected_res, "接口返回结果不符合预期")

    def test_xxjob_refundApply(self):
        '''
            执行 抖音店铺 的售后单拉取定时任务
        '''
        '''
            常用定时任务id：
            店铺 的售后单拉取定时任务
                抖音："id": "355"
                京东："id": "357"
                快手："id": "496"
                拼多多："id": "359"
                淘宝："id": "362"
                天猫："id": "1367"
            物流中台-拦截后置任务 创建erp补发单跑批
                "id": "1182"
            物流-主动跟单 订单拉取
                "id": "342"
            转寄服务调度服务 trade扫描
                "id": "1532"
        '''
        xxjob_tigger.xxjob_excute(self,job_id='355')


if __name__ == '__main__':
    unittest.main()
