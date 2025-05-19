import unittest
import common.commons as common
from common.Get_time import Get_time
from Base.Get_token import Get_token
from Base.Get_xxjob_token import Get_token as Get_xxjob_token
from config import config
from cases_api.lg_admin.lg_admin_updatePullTime import updatePullTime
from cases_api.xxjob.xxjob_tigger import xxjob_tigger


class MyTestCase(unittest.TestCase):
    '''
    拦退单拉取
    '''
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        cls.admin_token = Get_token.lg_artifact_admin_token()
        cls.xxjob_pre_token = Get_xxjob_token.lg_xxjob_pre_token()
    def test_1_lg_admin_updatePullTime_dy_refundApply(self):
        '''
        修改售后单拉取时间
        '''
        beginTime = Get_time.before_now(self)
        endTime = Get_time.now(self)
        # 三青小小号公司-【抖音】松山棉店内衣旗舰店的售后单拉取时间
        updatePullTime.lg_admin_company_updatePullTime(self,
                                                       companyId="1896075670343610370",
                                                       order_task_id="1922574260093542402",
                                                       sellerId="1922574256859734017",
                                                       dataName="refundApply",
                                                       beginTime="2025-05-16 14:33:13",
                                                       endTime="2025-05-16 14:33:13"
                                                       )


    def test_2_xxjob_dy_refundApply(self):
        '''
        执行 抖音店铺 的售后单拉取定时任务
            常用定时任务id：
            店铺 的售后单拉取定时任务
                抖音："id": "355"
                京东："id": "357"
                快手："id": "496"
                拼多多："id": "359"
                淘宝："id": "362"
                天猫："id": "1367"
        '''
        xxjob_tigger.xxjob_excute(self, job_id='355')

if __name__ == '__main__':
    unittest.main()
