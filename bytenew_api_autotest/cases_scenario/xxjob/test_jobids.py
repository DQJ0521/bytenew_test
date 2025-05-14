#_*_encoding:utf-8_*_
import json
import unittest
from Base.Base_Page import Base
from Base.Get_xxjob_token import Get_token
import common.commons as commons
import config.config as config
from common.data_extractor import extract_nested_ids

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logs = commons.Common().get_logs()
        cls.xxjob_pre_token = Get_token.lg_xxjob_pre_token()

    def test_jobids(self):
        '''
                获取定时任务id
        '''
        url = config.xxjob_host+"/jobinfo/pageList"
        header = {'Content-Type': 'application/x-www-form-urlencoded', "Cookie": self.xxjob_pre_token}
        method = 'POST'
        datas = {"jobGroup": "48","triggerStatus":"-1","start":"0","length":"10"}
        result = Base().requests_type(method=method, url=url, headers=header,data=datas)
        try:
            if result.status_code !=200:
                raise ValueError(f"请求失败，状态码: {result.status_code}")

            ids_list = json.loads(result.text)
            # 提取特定键值
            all_ids = extract_nested_ids(ids_list, key='id')
            self.logs.info(f"所有定时任务ID: {all_ids}")

        except Exception as e:
            print(f"[ERROR] 获取 id 失败: {str(e)}")


if __name__ == '__main__':
    unittest.main()
