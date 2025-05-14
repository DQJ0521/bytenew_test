from datetime import datetime, timedelta
#import datetime
import json
import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt
#from Base.Get_token_pre import Get_token
from Base.Base_test.Get_admin_token import Get_token
from common.Get_time import Get_time

@ddt.ddt
class MyTestCase(unittest.TestCase):
    cases = common.Common().ReadExcelTypeDict("lg_admin_update_cases.xlsx")
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.logs.info("========= 测试开始 =========")
        cls.admin_token = Get_token.lg_artifact_admin_pre_token()

        # cls.logs.info(f"获取到 Token: {cls.admin_token}")
        # if not cls.admin_token:
        #     raise ValueError("Token 获取失败，无法执行测试")
        # cls.logs.info(f"Token 获取成功: {cls.admin_token}")
    @ddt.data(*cases)
    def test_lg_admin_company_updatePullTime(self,pars):
        # 动态显示用例名称（从Excel读取）
        case_name = pars.get('casename')
        self.logs.info(f"▶▶▶ 执行用例: {case_name} ◀◀◀")
        #self.logs.debug(f"测试数据明细: {pars}")

        url = pars['url']
        headers = {'Content-Type': 'application/json',"token":self.admin_token }
        method = pars['请求方式']
        datas = json.loads(pars['body']) if isinstance(pars['body'], str) else pars['body'].copy()
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
