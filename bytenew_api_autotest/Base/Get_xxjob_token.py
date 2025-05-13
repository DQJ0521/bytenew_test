import hashlib
import json
from Base.Base_Page import Base
import re

class Get_token():
    """
        获取xxjob登录的Cookie
        :return:
    """
    _xxjob_token = None

    @classmethod
    def lg_xxjob_pre_token(cls):
        if cls._xxjob_token is None:
            try:
                s = Base()
                result = s.requests_type(
                    method='POST',
                    url='https://xjadmin-pre.bytenew.com/login',
                    headers={'Content-Type': 'application/x-www-form-urlencoded'},
                    data= "userName=habi&password=habi123"
                )

                # 检查 HTTP 状态码
                if result.status_code != 200:
                    raise ValueError(f"HTTP 状态码异常: {result.status_code}")

                # 提取 Token
                cookieHeader = result.cookies
                LOGIN_IDENTITY = cookieHeader.get("XXL_JOB_LOGIN_IDENTITY")
                cls._xxjob_token = f"XXL_JOB_LOGIN_IDENTITY={LOGIN_IDENTITY}"
                #print(f"[INFO] Token 已缓存: {cls._xxjob_token}")
            except Exception as e:
                print(f"[ERROR] 获取 Token 失败: {str(e)}")
                cls._xxjob_token = None
        return cls._xxjob_token