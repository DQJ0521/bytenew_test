# test_example.py
from Base.Base_db_demo import DB
import unittest
import common.commons as common


class DB_run(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logs = common.Common().get_logs()
    def test_database_operations(self):
        # 初始化数据库对象
        db = DB()

        try:
            # 连接数据库（使用默认MySQL配置）
            db.connect()

            # 执行参数化查询
            express_number = '8201158249113'
            sql = """
                SELECT a.problemparts_id, b.problem_state, b.deal_state 
                FROM ems.tapp_problem a 
                LEFT JOIN ems.temp_deal_status b 
                    ON a.problemparts_id = b.problem_id 
                WHERE a.problemparts_expressnumber = %s 
                ORDER BY a.problemparts_createdate DESC
            """
            result = db.select(sql, (express_number,))
            self.logs.info(f"查询结果: {result}")

        except Exception as e:
            print(f"数据库测试失败: {str(e)}")
        finally:
            db.close()


if __name__ == '__main__':
    unittest.main()