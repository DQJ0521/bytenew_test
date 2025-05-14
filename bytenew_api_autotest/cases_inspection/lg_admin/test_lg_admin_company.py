#_*_encoding:utf-8_*_
import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt
from Base.Get_token_pre import Get_token
#from Base.Base_test.Get_admin_token import Get_token


@ddt.ddt
class MyTestCase(unittest.TestCase):
    cases = common.Common().ReadExcelTypeDict("lg_admin_cases.xlsx")
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.logs.info("========= 测试开始 =========")
        cls.admin_token = Get_token.lg_artifact_admin_pre_token()

    @classmethod
    def tearDownClass(cls):
        cls.logs.info("========= 测试结束 =========")

    def setUp(self):
        self.logs.info(f"开始用例: {self._testMethodName }")

    def tearDown(self):
        self.logs.info(f"结束用例: {self._testMethodName }")
    @ddt.data(*cases)
    def test_lg_admin_company(self,pars):
        '''
            拉取公司列表，杭州云贝-店铺列表，杭州云贝-【淘宝】tb3062364902-订单拉取时间列表
        '''
        # 动态显示用例名称（从Excel读取）
        case_name = pars.get('casename')
        self.logs.info(f"▶▶▶ 执行用例: {case_name} ◀◀◀")
        #self.logs.debug(f"测试数据明细: {pars}")

        url = pars['url']
        header = {'Content-Type': 'application/json',"token":self.admin_token }
        params = pars['params']
        method = pars['请求方式']
        datas = pars['body']
        expected_res = pars['预期结果']

        result = Base().requests_type(method=method, url=url, headers=header,data=datas)
        #self.logs.info(f"响应数据：{result.json()}")

        self.assertEqual(result.json()['success'], expected_res, "接口返回结果不符合预期")

if __name__ == '__main__':
    unittest.main()
