from datetime import datetime, timedelta
#import datetime
import json
import unittest
import yaml
import common.commons as common
from Base.Base_Page import Base
from Base.Get_token import Get_token
#from Base.Base_test.Get_admin_token import Get_token
import config.config as config


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.logs.info("========= 测试开始 =========")
        cls.admin_token = Get_token.lg_artifact_admin_token()
        # with open('./config/url.yaml') as f:
        #     urls = yaml.load(f,loader=yaml.FullLoader)
        #     print(urls)


    def test_lg_admin_company_sellerlist(self):

        url = config.admin_host+ '/api/seller/pageList'
        headers = {'Content-Type': 'application/json',"token":self.admin_token }
        method = 'POST'
        data = {"pageNum":'1',"pageSize":'10',"total":'0',"sourceList":[],"sellerIdList":[],"companyId":"1896837922267267074"}
        #datas = json.loads(pars['body']) if isinstance(pars['body'], str) else pars['body'].copy()
        #self.logs.debug(f"data--->:{datas}")
        body = json.dumps(data)
        #self.logs.debug(f"body---->:{body}")

        result = Base().requests_type(method=method, url=url, headers=headers,data=body)
        self.logs.info(f"响应数据：{result.json()}")

        self.assertEqual(result.json()['success'], True, "接口返回结果不符合预期")


if __name__ == '__main__':
    unittest.main()
