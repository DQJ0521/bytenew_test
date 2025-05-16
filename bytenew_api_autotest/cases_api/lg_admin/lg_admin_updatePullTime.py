from datetime import datetime, timedelta
#import datetime
import json
import unittest
import yaml
import common.commons as common
from Base.Base_Page import Base
from Base.Get_token import Get_token
#from Base.Base_test.Get_admin_token import Get_token
from common.Get_time import Get_time
import config.config as config


class updatePullTime():
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        #cls.logs.info("========= 测试开始 =========")
        cls.admin_token = Get_token.lg_artifact_admin_token()

    def lg_admin_company_updatePullTime(self,companyId,order_task_id,sellerId,dataName,beginTime,endTime):

        url = config.admin_host+ "/api/seller/updatePullTime"
        headers = {'Content-Type': 'application/json',"token":self.admin_token }
        method = 'POST'
        datas ={
            "companyId": {companyId},
            "id":{order_task_id},
            "sellerId":{sellerId},
            "source":'1',
            "dataName":{dataName},
            "beginTime":{beginTime},
            "endTime":{endTime}
        }
        #self.logs.debug(f"data--->:{datas}")
        body = json.dumps(datas)
        self.logs.debug(f"body---->:{body}")

        result = Base().requests_type(method=method, url=url, headers=headers,data=body)
        #self.logs.info(f"响应数据：{result.json()}")

        #self.assertEqual(result.json()['success'], True, "接口返回结果不符合预期")


