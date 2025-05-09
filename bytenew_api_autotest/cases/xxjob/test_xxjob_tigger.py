#_*_encoding:utf-8_*_
import unittest
from Base.Base_Page import Base
from Base.Get_xxjob_token import Get_token
import common.commons as commons
import ddt
import config.config as config

class MyTestCase(unittest.TestCase):

    #cases = commons.Common.ReadExcelTypeDict("")

    @classmethod
    def setUpClass(cls):
        cls.logs = commons.Common().get_logs()
        cls.xxjob_pre_token = Get_token.lg_xxjob_pre_token()

    #@ddt.data(*cases)
    def test_xxjob_dy_refundApply(self):
        '''
                执行 抖音店铺 的售后单拉取定时任务
        '''
        url = config.xxjob_host+"/jobinfo/trigger"
        header = {'Content-Type': 'application/x-www-form-urlencoded', "Cookie": self.xxjob_pre_token}
        method = 'POST'
        datas = {"id": "355","executorParam":"","addressList":""}
        result = Base().requests_type(method=method, url=url, headers=header,data=datas)
        self.logs.info(f"请求数据：{result.request.body}")
        self.logs.info(f"响应结果：{result.text}")

        #assert result.status_code == 200
        self.assertEqual(result.status_code,200,"接口执行失败")



if __name__ == '__main__':
    unittest.main()
