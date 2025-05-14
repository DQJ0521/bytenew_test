# test_demo.py
import unittest
import logging
from Base.Base_db import DB
import common.commons as common

class DB_run(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.logs = common.Common().get_logs()

    def test_mysql_operations(self):
        """测试 MySQL 数据库操作"""
        db = DB()
        try:
            # 方式1：通过配置名称连接
            db.connect(config_name='mysql_banniu_book')
            expressnumber = "9831473717905"

        # 执行查询
            result = db.execute_query("SELECT * FROM ems.tapp_problem WHERE problemparts_expressnumber = %s", (expressnumber,))
            print(f"查询结果1: {result}")
            #print(f"查询结果: {result}")

        finally:
            db.close()


    def test_postgres_operations(self):
        """测试 PostgreSQL 数据库操作"""
        db = DB()
        try:
        # 方式2：动态参数连接 (无需配置名称)
            db.connect(
            db_type='postgresql',
            host='101.126.55.217',
            user='logistics',
            password='lg123456',
            database='artifact',
            port='54321'
            )

            trade_id = "2544918603427266691"

        # 执行更新
            rows = db.execute_query("SELECT * FROM artifact.intercept_order.intercept_order_1896837922267267074 WHERE trade_id =%s",(trade_id,))
            print(f"查询结果2: {rows}")

        finally:
            db.close()


if __name__ == "__main__":
    unittest.main()