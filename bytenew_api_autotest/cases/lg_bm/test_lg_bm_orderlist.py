#_*_encoding:utf-8_*_
import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt
#from config import config
from Base.Get_token_pre import Get_token
@ddt.ddt
class MyTestCase(unittest.TestCase):

    cases = common.Common().ReadExcelTypeDict("lg_bm_cases.xlsx")
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.logs.info("========= 测试开始 =========")
        cls.bm_cookie = Get_token.lg_bm_pre_token()
        # cls.logs.info(f"cookie获取结果: {cls.bm_cookie}")
        # if not cls.bm_cookie:
        #     raise ValueError("Token 获取失败，无法执行测试")
        # cls.logs.info(f"Token 获取成功: {cls.bm_cookie}")

    @classmethod
    def tearDownClass(cls):
        cls.logs.info("========= 测试结束 =========")

    def setUp(self):
        self.logs.info(f"开始用例: {self._testMethodName}")

    def tearDown(self):
        self.logs.info(f"结束用例: {self._testMethodName}")

    @ddt.data(*cases)
    def test_bm_intercept_order(self,pars):
        # 动态显示用例名称（从Excel读取）
        case_name = pars.get('casename')
        self.logs.info(f"▶▶▶ 执行用例: {case_name} ◀◀◀")
        self.logs.debug(f"测试数据明细: {pars}")

        url = pars['url']
        header = {'Content-Type': 'application/json','lg-bm-client':'1',"lg-bm-token":self.bm_cookie}
        #self.logs.info(f"[DEBUG] 实际请求头: {header}")
        method = pars['请求方式']
        datas = pars['body']
        expected_res = pars['预期结果']

        result = Base().requests_type(method=method, url=url, headers=header,data=datas)
        self.logs.info(f"响应结果：{result.json()}")

        self.assertEqual(result.json()['success'],expected_res,"接口返回结果不符合预期")


if __name__ == '__main__':
    unittest.main()
