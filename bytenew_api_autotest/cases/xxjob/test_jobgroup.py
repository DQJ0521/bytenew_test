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
    def test_jobgroup_pageList(self):
        url = config.xxjob_host + "/jobgroup/pageList?appname&title&start=0&length=200"
        header = {'Content-Type': 'application/json', "Cookie": self.xxjob_pre_token}
        self.logs.info(f"[DEBUG] 实际请求头: {header}")
        method = 'POST'

        result = Base().requests_type(method=method, url=url, headers=header)
        res = result.text
        self.logs.info(f"响应结果：{res}")

        try:
            if result.status_code !=200:
                raise ValueError(f"获取失败，状态码: {result.status_code}")




        except Exception as e:
            print(f"[ERROR] 获取 Grouplist_id 失败: {str(e)}")

if __name__ == '__main__':
    unittest.main()
