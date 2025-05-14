import hashlib
import json
from Base.Base_Page import Base
import re

class Get_token():
    """
        ----未完成----
        获取物流神器-4.0登录的token
        :return:
    """
    _artifact_token = None

    @classmethod
    def lg_artifact_pre_token(cls):
        """
            获取xxjob登录的Cookie
            :return:
        """
        if cls._artifact_token is None:
            try:
                s = Base()
                result = s.requests_type(
                    method='POST',
                    url='https://newbeta.bytenew.com/v2/logins/unifiedLogin',
                    headers={'Content-Type': 'application/json','lg-artifact-client':'2'},
                    data= {"mobile":"13559902336","password":"da04e0f7192694832b8174b72fb480ef","code":"","fp":"3688ab34ac5b71ae9c7b35d46e5ff535"}
                )

                # 检查 HTTP 状态码
                if result.status_code != 200:
                    raise ValueError(f"HTTP 状态码异常: {result.status_code}")

                # 提取 Token
                cookieHeader = result.cookies
                LOGIN_IDENTITY = cookieHeader.get("XXL_JOB_LOGIN_IDENTITY")
                cls._artifact_token = f"XXL_JOB_LOGIN_IDENTITY={LOGIN_IDENTITY}"
                print(f"[INFO] Token 已缓存: {cls._artifact_token}")
            except Exception as e:
                print(f"[ERROR] 获取 Token 失败: {str(e)}")
                cls._artifact_token = None
        return cls._artifact_token