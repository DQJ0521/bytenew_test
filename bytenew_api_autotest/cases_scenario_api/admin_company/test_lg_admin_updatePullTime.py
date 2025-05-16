from datetime import datetime, timedelta
#import datetime
import json
import unittest
import common.commons as common
from Base.Base_Page import Base
import ddt
from Base.Get_token import Get_token
#from Base.Base_test.Get_admin_token import Get_token
from common.Get_time import Get_time
import config.config as config
from cases_api.lg_admin.lg_admin_updatePullTime import updatePullTime


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        #cls.logs.info("========= 测试开始 =========")
        cls.admin_token = Get_token.lg_artifact_admin_token()

    def test_lg_admin_company_updatePullTime(self):
        updatePullTime.lg_admin_company_updatePullTime(self,
            companyId="1896075670343610370",
            order_task_id="1922574260093542402",
            sellerId="1922574256859734017",
            dataName="refundApply",
            beginTime="2025-05-16 14:33:13",
            endTime="2025-05-16 14:33:13"
        )




if __name__ == '__main__':
    unittest.main()
