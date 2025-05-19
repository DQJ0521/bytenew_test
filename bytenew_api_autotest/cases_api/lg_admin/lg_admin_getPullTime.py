import json

import common.commons
import config.config as config
from Base.Get_token import Get_token
from Base.Base_Page import Base
import common.commons as common
class getPullTime():
    '''
    根据店铺id获取该店铺下所有订单拉取更新时间
    '''
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common.get_logs()
        cls.admin_token = Get_token.lg_artifact_admin_token()

    def lg_admin_getPullTime(self,sellerId):
        url = config.admin_host + "/api/seller/getPullTime"
        headers = {'Content-Type': 'application/json', "token": self.admin_token}
        method = 'POST'
        body =json.dumps({"sellerId": sellerId})

        result = Base().requests_type(method=method, url=url, headers=headers, data=body)
        #self.logs.info(f"返回结果----》{result.json()}")
        return result

