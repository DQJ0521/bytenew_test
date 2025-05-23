import unittest
import common.commons as common
from Base.Get_token import Get_token
from cases_api.lg_admin.lg_admin_company_seller_list import list

class MyTestCase(unittest.TestCase):
    '''
    根据提供的companyId 判断是否开启了erp
    '''
    def test_lg_admin_companylist(self):
        res = list.lg_admin_companylist(companyId="1896075670343610370")
        try:
            record_list = res['data']['records'][0]

            # 检查openErp字段是否存在
            if 'openErp' in record_list:
                self.openErp = record_list['openErp']

                # 根据状态值打印日志
                if self.openErp == 1:
                    print("【成功】ERP系统状态: 已开启")
                elif self.openErp == 0:
                    print("【成功】ERP系统状态: 未开启")
                else:
                    print(f"【警告】未知ERP状态码: {self.openErp}")
            else:
                print("【错误】响应数据缺少openErp字段")
                self.openErp = None

        except Exception as e:
            print(f"【异常】数据解析失败: {str(e)}")
            self.openErp = None

if __name__ == '__main__':
    unittest.main()
