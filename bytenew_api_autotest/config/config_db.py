#_*_encoding:utf-8_*_
'''
    pre：DEBUG = 1
    prod：DEBUG = 2
'''
DEBUG = 1
failed,passed,error,rerun = 0,0,0,0
if DEBUG == 1:
    DB_CONFIGS = {
    # MySQL (诺客测试环境)配置
    'mysql_banniu_book': {
        'db_type': 'mysql',
        'host': '101.126.55.217',
        'user': 'nktest',
        'password': 'BNuokeBE_IxIAjTesT',
        'database': 'banniu_book',
        'port': 3306,
        'charset': 'utf8'
    },

    # PostgreSQL （快递神器测试环境） 配置
    'postgres_artifact': {
        'db_type': 'postgresql',
        'host': '101.126.55.217',
        'user': 'logistics',
        'password': 'lg123456',
        'database': 'artifact',
        'port': 54321
    },

    # PostgreSQL （快递神器预发订单） 配置
    'postgres_artifact_pre': {
        'db_type': 'postgresql',
        'host': '101.126.55.217',
        'user': 'logistics',
        'password': 'lg123456',
        'database': 'artifact',
        'port': 54320
    }
    # 其他数据库配置...
    }