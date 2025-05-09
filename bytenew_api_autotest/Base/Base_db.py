# -*- coding: UTF-8 -*-
import MySQLdb
import psycopg2
import runs

import common.commons as commons

class DB():

    @classmethod
    def db_connect(cls, db_banniu_book_conn=None):
        cls.logs = commons.Common.get_logs()
        # 诺客测试环境（banniu_book）
        cls.db_banniu_book_conn = MySQLdb.connect('101.126.55.217', 'nktest', 'BNuokeBE_IxIAjTesT', 'banniu_book', charset='utf8')
        cls.banniu_book_cursor = db_banniu_book_conn.cursor()

    def db_select(self):
        expressnumber = '8201158249113'

        sql_deal_status = "select a.problemparts_id,b.problem_state,b.deal_state from ems.tapp_problem a left join ems.temp_deal_status b on a.problemparts_id = b.problem_id where a.problemparts_expressnumber = %s ORDER BY a.problemparts_createdate DESC" % expressnumber
        self.banniu_book_cursor.execute(sql_deal_status)
        res = self.banniu_book_cursor.fetchone()
        self.logs.info(f"执行结果：{res}")


    def db_close(self):
        self.banniu_book_cursor.close()

