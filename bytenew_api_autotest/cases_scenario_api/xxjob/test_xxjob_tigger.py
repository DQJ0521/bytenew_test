#_*_encoding:utf-8_*_
import unittest
from Base.Base_Page import Base
from Base.Get_xxjob_token import Get_token
import common.commons as commons
import ddt
import config.config as config
from cases_api.xxjob.xxjob_tigger import xxjob_tigger

class MyTestCase(unittest.TestCase):

    def test_xxjob_dy_refundApply(self):
        '''
            常用定时任务id：
            店铺 的售后单拉取定时任务
                抖音："id": "355"
                京东："id": "357"
                快手："id": "496"
                拼多多："id": "359"
                淘宝："id": "362"
                天猫："id": "1367"
            物流中台-拦截后置任务 创建erp补发单跑批
                "id": "1182"
            物流-主动跟单 订单拉取
                "id": "342"
            转寄服务调度服务 trade扫描
                "id": "1532"
        '''
        res = xxjob_tigger.trigger_job( job_id='355')
        self.assertEqual(res.get('code'),200,"接口请求异常")


if __name__ == '__main__':
    unittest.main()
