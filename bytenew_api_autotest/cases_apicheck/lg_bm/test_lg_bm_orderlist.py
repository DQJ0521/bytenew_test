#_*_encoding:utf-8_*_
import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt
from Base.Get_token import Get_token
#from Base.Base_test.Get_bm_token import Get_token
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
        cls.bm_cookie = Get_token.lg_bm_token()

    @classmethod
    def tearDownClass(cls):
        cls.logs.info("========= 测试结束 =========")

    def setUp(self):
        self.logs.info(f"开始用例: {self._testMethodName}")

    def tearDown(self):
        self.logs.info(f"结束用例: {self._testMethodName}")

    @ddt.data(*cases)
    def test_bm_orderlist(self,pars):
        self._testMethodDoc = pars.get('casename', '默认用例描述')
        # # 动态显示用例名称（从Excel读取）
        # case_name = pars.get('casename')
        # self.logs.info(f"▶▶▶ 执行用例: {case_name} ◀◀◀")

        url = config.bm_host+ pars['url']
        header = {'Content-Type': 'application/json','lg-bm-client':'1',"lg-bm-token":self.bm_cookie}
        method = pars['请求方式']
        datas = pars['body']
        expected_res = pars['预期结果']

        result = Base().requests_type(method=method, url=url, headers=header,data=datas)

        # "status_code检查"
        self.assertEqual(result.status_code, 200, f"请求失败,状态码: :{result.status_code}")

        # 检查响应结果
        self.assertEqual(result.json()['success'],expected_res,"接口返回结果不符合预期")




if __name__ == '__main__':
    unittest.main()
