from datetime import datetime, timedelta
#import datetime
import json
import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt
from Base.Get_token import Get_token
#from Base.Base_test.Get_admin_token import Get_token
from common.Get_time import Get_time
import config.config as config

@ddt.ddt
class MyTestCase(unittest.TestCase):
    '''
    修改店铺的订单拉取时间
    店铺及订单类型信息从excel表格中获取，并执行所有
    '''
    cases = common.Common().ReadExcelTypeDict("lg_admin_update_cases.xlsx")
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.logs.info("========= 测试开始 =========")
        cls.admin_token = Get_token.lg_artifact_admin_token()

    @ddt.data(*cases)
    def test_lg_admin_company_updatePullTime(self,pars):
        # 动态显示用例名称（从Excel读取）
        case_name = pars.get('casename')
        self.logs.info(f"▶▶▶ 执行用例: {case_name} ◀◀◀")
        #self.logs.debug(f"测试数据明细: {pars}")

        url = config.admin_host+ pars['url']
        headers = {'Content-Type': 'application/json',"token":self.admin_token }
        method = pars['请求方式']
        datas = json.loads(pars['body']) if isinstance(pars['body'], str) else pars['body'].copy()
        # datas['companyId'] = config.admin_companyId
        # datas['id'] = config.order_task_id
        # datas['sellerId'] = config.sellerId
        # 获取当前时间并减 1 分钟
        datas['beginTime'] = Get_time.before_now(self)
        # 获取当前时间
        datas['endTime'] = Get_time.now(self)
        #self.logs.debug(f"data--->:{datas}")
        body = json.dumps(datas)
        #self.logs.debug(f"body---->:{body}")
        expected_res = pars['预期结果']

        result = Base().requests_type(method=method, url=url, headers=headers,data=body)
        #self.logs.info(f"响应数据：{result.json()}")

        self.assertEqual(result.json()['success'], expected_res, "接口返回结果不符合预期")


if __name__ == '__main__':
    unittest.main()
