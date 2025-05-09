# -*- coding: UTF-8 -*-
import MySQLdb
import psycopg2


#诺客测试环境（banniu_book）
db = MySQLdb.connect('101.126.55.217','nktest','BNuokeBE_IxIAjTesT','banniu_book',charset='utf8')
cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database version : %s "%data)

expressnumber = '8201158249113'

sql_deal_status = "select a.problemparts_id,b.problem_state,b.deal_state from ems.tapp_problem a left join ems.temp_deal_status b on a.problemparts_id = b.problem_id where a.problemparts_expressnumber = %s ORDER BY a.problemparts_createdate DESC"%expressnumber
cursor.execute(sql_deal_status)
res = cursor.fetchone()
print(res)

#sql_deal_success = "INSERT INTO `ems`.`temp_deal_status` (`id`, `problem_id`, `problem_state`, `deal_state`, `logistics_state`, `state`, `created_time`, `operate_time`, `count`, `msg`, `memo`, `problem_state_code`, `deal_state_code`, `logistics_state_code`, `collection_network`, `scan_type`, `scan_text`, `scan_time`)  SELECT NULL, problemparts_id, '处理中', '拦截成功', NULL, 0, NOW(), NOW(), 0, NULL, NULL, 'problemState_1', 'dealState_2', NULL, NULL, NULL, NULL, NULL  FROM ems.tapp_problem WHERE problemparts_expressnumber = %s ORDER BY problemparts_createdate DESC LIMIT 1"%expressnumber
#cursor.execute(sql_deal_success)
# data2 = cursor.fetchone()
# print(data2)
db.close()

