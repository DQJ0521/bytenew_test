import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt

import config.config as config
#from Base.Get_token_pre import Get_token
from Base.Base_test.Get_cw_token import Get_token


@ddt.ddt
class MyTestCase(unittest.TestCase):
    cases = common.Common().ReadExcelTypeDict("lg_cw_cases.xlsx")
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.logs.info("========= 测试开始 =========")
        cls.cw_token = Get_token.lg_cw_pre_token()
        # if not cls.cw_token:
        #     raise ValueError("Token 获取失败，无法执行测试")
        # cls.logs.info(f"Token 获取成功: {cls.cw_token}")
        # cls.logs.info(f"获取到 Token: {cls.cw_token}")

    @classmethod
    def tearDownClass(cls):
        cls.logs.info("========= 测试结束 =========")

    def setUp(self):
        self.logs.info(f"开始用例: {self._testMethodName}")

    def tearDown(self):
        self.logs.info(f"结束用例: {self._testMethodName}")
    @ddt.data(*cases)
    def test_lg_cw_redirect_list(self,pars):
        self.logs.info(f"测试数据:{pars}")
        url = config.cw_host+ pars['url']
        header = {'Content-Type': 'application/json',"lg-cw-token":self.cw_token,'lg-cw-client': '1' }
        method = pars['请求方式']
        datas = pars['body']
        expected_res = pars['预期结果']

        result = Base().requests_type(method=method, url=url, headers=header, data=datas)
        self.logs.info(f"响应数据：{result.json()}")

        self.assertEqual(result.json()['success'], expected_res, "接口返回结果不符合预期")

if __name__ == '__main__':
    unittest.main()
