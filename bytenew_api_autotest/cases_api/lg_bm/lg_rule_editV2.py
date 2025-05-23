import json
import unittest
import datetime

import common.commons
import config.config as config
from Base.Get_token import Get_token
from Base.Base_Page import Base
import common.commons as commons
class rule_editV2(unittest.TestCase):
    '''
    编辑拦截规则
    '''
    _bm_token = None
    @classmethod
    def _init_token(cls):
        if not cls._bm_token:
            cls._bm_token = Get_token.lg_bm_token()

    def lg_bm_rule_editV2(self,
                          ruleid,
                          ruleName,
                          sellerIds,
                          scopeRuleContent,
                          interceptRuleContent,
                          delayRuleContent,
                          refundRuleContent,
                          tradeMemoRuleContent,
                          buyerNotifyRuleContent,
                          collaborativeNotifyRuleContent):

        self._init_token()
        url = config.bm_host + "/api/rule/editV2"
        headers = {'Content-Type': 'application/json','lg-bm-client':'1',"lg-bm-token":self._bm_token}
        method = 'POST'
        body =json.dumps({
            "id":ruleid,
            "ruleName": ruleName,
            "sellerIds":sellerIds,
            "validTimeBegin":datetime.date,
            "validTimeEnd":"2099-12-31",
            "scopeRuleContent":scopeRuleContent,
            "interceptRuleContent":interceptRuleContent,
            "delayRuleContent":delayRuleContent,
            "refundRuleContent":refundRuleContent,
            "tradeMemoRuleContent":tradeMemoRuleContent,
            "buyerNotifyRuleContent":buyerNotifyRuleContent,
            "collaborativeNotifyRuleContent":collaborativeNotifyRuleContent,
            "bizType":1,
            "version":2
        })

        result = Base().requests_type(method=method, url=url, headers=headers, data=body)
        commons.Common.get_logs().info(f"返回结果----》{result.json()}")
        return result

    # def test_lg_bm_rule_getListByAll(self):
    #     self.lg_bm_rule_editV2()



