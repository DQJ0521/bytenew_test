#import datetime
import unittest
import time
import common.commons as common
from Base.Get_token import Get_token
from cases_api.lg_admin.lg_admin_getPullTime import getPullTime
from cases_api.lg_admin.lg_admin_updatePullTime import updatePullTime
from common.Get_time import Get_time
from config.JobConfig import JobConfig
from cases_api.xxjob.xxjob_tigger import xxjob_tigger

class MyTestCase(unittest.TestCase):
    '''
    根据提供的sellerId和dataName可以获取到companyId和order_task_id，source。作为更新拉取时间和执行定时任务的条件。
    更新售后单拉取时间-》执行定时任务
    '''
    target_company_id = None
    target_order_task_id = None
    target_source = None
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
        #cls.logs.info("========= 测试开始 =========")
        cls.admin_token = Get_token.lg_artifact_admin_token()
        #指定要执行的店铺id和订单数据类型
        cls.sellerId = "1914975657167839234"
        cls.dataName = "refundApply"

        #更新售后单时间设置
        #cls.beginTime = Get_time.before_now() # 获取当前时间并减 2 分钟
        cls.beginTime = "2025-05-23 13:37:00"
        #cls.endTime = Get_time.now() # 获取当前时间
        cls.endTime = "2025-05-23 13:38:59"

        #直接设置job_id
        cls.id = '1568'

    def test_1_lg_admin_getPullTime(self):
        """
        获取指定dataName的companyId和order_task_id
        """
        #调用获取接口
        res = getPullTime.lg_admin_getPullTime(self,sellerId=self.sellerId)
        #print(res.json())
        self.assertEqual(res.status_code,200,"接口请求失败")
        # 解析响应数据
        try:
            data_list = res.json().get('data', [])
            if not data_list:
                self.fail("返回数据为空")
            # 解析响应数据
            target_data = next(
                (item for item in data_list
                 if item.get('dataName') == self.dataName),
                None
            )
            if not target_data:
                self.fail(f"没有获取到：{self.dataName}的数据")
            # 存储到类属性
            self.__class__.target_company_id = target_data['companyId']
            self.__class__.target_order_task_id = target_data['id']
            self.__class__.target_source = target_data['source']

            self.logs.info(
                f"成功获取参数: companyId={self.target_company_id}, "
                f"order_task_id={self.target_order_task_id},"
                f"source={self.target_source}"
            )

        except Exception as e:
            print(f"[ERROR] 获取 店铺订单拉取时间 失败: {str(e)}")

    def test_2_lg_admin_company_updatePullTime(self):
        """使用前一个测试方法获取的参数更新售后单拉取时间"""
        # 检查参数是否已获取
        if not self.target_company_id or not self.target_order_task_id:
            self.skipTest("未获取到必要参数，跳过此测试")

        updateres = updatePullTime.lg_admin_company_updatePullTime(self,
            companyId=self.target_company_id,
            order_task_id=self.target_order_task_id,
            sellerId=self.sellerId,
            dataName=self.dataName,
            beginTime=self.beginTime,
            endTime=self.endTime
        )

        self.assertEqual(updateres.status_code,200,"更新请求失败")
        self.assertTrue(updateres.json().get('success'),"更新操作未成功")

    def test_3_trigger_refund_job(self):
        # """使用第一个测试方法获取的source匹配job_id，执行定时任务"""
        # # 等待5秒
        time.sleep(5)

        try:
            # 参数是否已获取
            if not self.target_source:
                job_id = self.id
            else:
                # 根据source匹配job_id
                job_id = JobConfig.get_job_id(source=self.target_source)
                print(f"获取到的job_id:{job_id}")
            # 调用任务触发接口
            xxjob_tigger.trigger_job(job_id=job_id)
        except Exception as e:
            print(f"执行失败")
        #xxjob_tigger.trigger_job(job_id='1568')

if __name__ == '__main__':
    unittest.main()
