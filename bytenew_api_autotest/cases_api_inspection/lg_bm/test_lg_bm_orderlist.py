#_*_encoding:utf-8_*_
import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt
from Base.Get_token_pre import Get_token
#from Base.Get_token_test.Get_bm_token import Get_token
import config.config as config
@ddt.ddt
class MyTestCase(unittest.TestCase):
    """
        班门 - 查询公司（三青小小号公司）各类工单记录列表
    """
    cases = common.Common().ReadExcelTypeDict("lg_bm_list_cases.xlsx")
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.logs.info("========= 测试开始 =========")
        cls.bm_cookie = Get_token.lg_bm_pre_token()

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

        url = config.bm_host+ pars['url']
        header = {'Content-Type': 'application/json','lg-bm-client':'1',"lg-bm-token":self.bm_cookie}
        #self.logs.info(f"[DEBUG] 实际请求头: {header}")
        method = pars['请求方式']
        datas = pars['body']
        expected_res = pars['预期结果']

        result = Base().requests_type(method=method, url=url, headers=header,data=datas)
        self.logs.info(f"响应结果：{result.status_code}")

        self.assertEqual(result.json()['success'],expected_res,"接口返回结果不符合预期")


if __name__ == '__main__':
    unittest.main()
