#_*_encoding:utf-8_*_
from Base.Base_Page import Base
from Base.Get_xxjob_token import Get_token
import common.commons as commons
import config.config as config

class xxjob_tigger():
    @classmethod
    def setUpClass(cls):
        cls.logs = commons.Common().get_logs()
        cls.xxjob_pre_token = Get_token.lg_xxjob_pre_token()

    #@ddt.data(*cases)
    def xxjob_excute(self,job_id):

        url = config.xxjob_host+"/jobinfo/trigger"
        header = {'Content-Type': 'application/x-www-form-urlencoded', "Cookie": self.xxjob_pre_token}
        method = 'POST'
        datas = {"id": {job_id},"executorParam":"","addressList":""}
        result = Base().requests_type(method=method, url=url, headers=header,data=datas)
        self.logs.info(f"请求数据：{result.request.body}")
        self.logs.info(f"响应结果：{result.text}")

        #assert result.status_code == 200
        #self.assertEqual(result.status_code,200,"接口执行失败")
        return result

