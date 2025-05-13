#_*_encoding:utf-8_*_
'''
    pre：DEBUG = 1
    prod：DEBUG = 2
'''

DEBUG = 1
failed,passed,error,rerun = 0,0,0,0
if DEBUG == 1:
    #云仓系统
    cw_host = "https://lg-cw-pre.bytenew.com"
    cw_mobile = "13588888888"
    cw_loginPwd = "YC888888"

    #admin系统
    admin_host = "https://lg-artifact-admin-pre.bytenew.com"
    admin_loginName = "admin"
    admin_loginPwd = "lg123456"

    #快递神器4.0
    artifact_host = ""
    artifact_cookie = ""

    #班门5.0
    bm_host = "https://lg-bm-login-pre.bytenew.com"
    bm_mobile = "19855555555"
    bm_loginPwd = "555555"

    #xxjob
    xxjob_host = "https://xjadmin-pre.bytenew.com"
    xxjob_pre_Cookie=""

    #公司、店铺信息 ：
    #公司
    admin_companyId = "1896837922267267074" #杭州云贝
    #店铺
    sellerId = "1896837929762488321" #【抖音】紫貂的小店
    #sellerId = "1914273297125564418" #【淘宝】tb3062364902
    order_task_id = "1914579714764136449" #tradePay：异常物流、主动拉取销售订单
    #order_task_id = "1914273304511733762" #refundApply ：售后单拉取
    #order_task_id = "1914579738050912258" #exchangePull ：
    #order_task_id = "1914579763996876801" #tradeAnalysis ：
    #order_task_id = "1914579714663473154" #refundPull ：


elif DEBUG == 2:
    #云仓系统
    cw_host = "https://warehouse.bytenew.com/"
    cw_mobile = "13588766396"
    cw_loginPwd = "YC766396"

    #admin系统
    admin_host = "https://express-admin.bytenew.com/"
    admin_loginName = "admin"
    admin_loginPwd = "lg123456"

    #快递神器4.0
    artifact_host = ""
    artifact_cookie = ""

    #班门5.0
    bm_host = "https://work-bm.bytenew.com/"
    bm_mobile = "15799999995"
    bm_loginPwd = "999995"

    #xxjob
    xxjob_host = "https://xjadmin-lg.bytenew.com"
    xxjob_pre_Cookie=""






