import json
import unittest

import common.commons
import config.config as config
from Base.Get_token import Get_token
from Base.Base_Page import Base
import common.commons as commons
class rule_getListByAll(unittest.TestCase):
    '''
    获取店铺的拦截规则
    '''
    _bm_token = None
    @classmethod
    def setUpClass(cls):
        cls.logs = commons.Common.get_logs(cls)
        cls._bm_token = Get_token.lg_bm_token()

    def lg_bm_rule_getListByAll(self):
        url = config.bm_host + "/api/rule/getListByAllV2"
        headers = {'Content-Type': 'application/json','lg-bm-client':'1',"lg-bm-token":self._bm_token}
        method = 'POST'
        body ={}

        result = Base().requests_type(method=method, url=url, headers=headers, data=body)
        #self.logs.info(f"返回结果----》{result.json()}")
        return result

    def find_seller_data(self,response_data: dict, target_seller_id: str) -> dict:
        """
        在响应数据中查找包含指定 sellerId 的条目

        :param response_data: 接口返回的字典数据
        :param target_seller_id: 要查找的sellerId值
        :return: 匹配到的完整数据条目（字典格式），若未找到返回None
        """
        # 检查数据结构有效性
        if not isinstance(response_data.get('data'), list):
            raise ValueError("响应数据格式异常，data字段应为列表类型")

        # 遍历data列表查找匹配项
        for item in response_data['data']:
            # 安全获取sellerIds字段
            seller_ids = item.get('sellerIds', [])

            # 检查是否为列表类型
            if not isinstance(seller_ids, list):
                continue  # 跳过无效数据

            # 精确匹配目标sellerId（字符串类型完全匹配）
            if target_seller_id in seller_ids:
                return item

        return None  # 未找到匹配项

    def test_lg_bm_rule_getListByAll(self):
        response = self.lg_bm_rule_getListByAll().json()
        #print(response)
        target_id = '1916411141249196034'
        matched_data = self.find_seller_data(response, target_id)

        if matched_data:
            print(f"找到匹配数据:{matched_data}")
            # print(f"ID: {matched_data['id']}")
            # print(f"规则名称: {matched_data['ruleName']}")
            # print(f"Seller列表: {matched_data['sellerIds']}")
        else:
            print("未找到匹配数据")



