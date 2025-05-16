import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt

import config.config as config
from Base.Get_token import Get_token
#from Base.Base_test.Get_cw_token import Get_token


@ddt.ddt
class MyTestCase(unittest.TestCase):
    cases = common.Common().ReadExcelTypeDict("lg_cw_cases.xlsx")
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.logs.info("========= 测试开始 =========")
        cls.cw_token = Get_token.lg_cw_token()


    @classmethod
    def tearDownClass(cls):
        cls.logs.info("========= 测试结束 =========")

    def setUp(self):
        self.logs.info(f"开始用例: {self._testMethodName}")

    def tearDown(self):
        self.logs.info(f"结束用例: {self._testMethodName}")
    @ddt.data(*cases)
    #@ddt.unpack
    def test_lg_cw_redirect_list(self,pars):
        self._testMethodDoc = pars.get('casename', '默认用例描述')
        url = config.cw_host+ pars['url']
        header = {'Content-Type': 'application/json',"lg-cw-token":self.cw_token,'lg-cw-client': '1' }
        method = pars['请求方式']
        datas = pars['body']
        expected_res = pars['预期结果']

        result = Base().requests_type(method=method, url=url, headers=header, data=datas)

        #"Http Code检查"
        self.assertEqual(result.status_code,200,f"请求失败,状态码: :{result.status_code}")

        #检查响应时间
        #self.logs.info(f"响应时长：{result.duration}")
        #assert self.response['duration'] < 1500

        #返回数据校验
        self.assertEqual(result.json()['success'], expected_res, "接口返回结果不符合预期")

if __name__ == '__main__':
    unittest.main()
