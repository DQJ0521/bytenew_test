#_*_encoding:utf-8_*_
from Base.Get_token_pre import Get_token

DEBUG = 1
failed,passed,error,rerun = 0,0,0,0
if DEBUG == 1:
    #云仓系统
    cw_host = "https://lg-cw-pre.bytenew.com"
    cw_token = Get_token.lg_cw_pre_token()

    #admin系统
    admin_host = "https://lg-artifact-admin-pre.bytenew.com"
    admin_token = Get_token.lg_artifact_admin_pre_token()

    #快递神器4.0
    artifact_host = ""
    artifact_cookie = ""

    #班门5.0
    bm_host = "https://lg-bm-login-pre.bytenew.com"
    bm_cookie = Get_token.lg_bm_pre_token()

    #xxjob
    xxjob_host = "https://xjadmin-pre.bytenew.com"
    xxjob_pre_Cookie=""




