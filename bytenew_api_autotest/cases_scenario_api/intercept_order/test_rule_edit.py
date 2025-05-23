import unittest
import cases_api.lg_bm.lg_rule_editV2 as lg_rule_editV2
class MyTestCase(unittest.TestCase):
    def test_rule_edit(self):
        lg_rule_editV2.rule_editV2(self,
                                   ruleid="1922188917779947522",
                                   ruleName="哈比的淘宝店",
                                   sellerIds=["1916411141249196034"],
                                   scopeRuleContent={},
                                   interceptRuleContent={},
                                   delayRuleContent={},
                                   refundRuleContent={},
                                   tradeMemoRuleContent={},
                                   buyerNotifyRuleContent={},
                                   collaborativeNotifyRuleContent={}
                                   )

if __name__ == '__main__':
    unittest.main()
