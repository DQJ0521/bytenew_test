#_*_encoding:utf-8_*_
import hashlib
import unittest
import json
from Base.Base_Page import Base
import config.config as config

class Get_token():
    # 类属性缓存不同服务的 Token
    _cw_token = None
    _admin_token = None
    _artifact_token = None
    _bm_token = None

    @classmethod
    def lg_cw_token(cls):
        """
            获取云仓登录的token
            :return:
        """
        if cls._cw_token is None:
            try:
                s = Base()
                result = s.requests_type(
                    method='POST',
                    url=config.cw_host+'/api/user/normalUserLogin',
                    headers={'lg-cw-client': '1', 'Content-Type': 'application/json'},
                    data=json.dumps({"mobile": config.cw_mobile, "loginPwd": config.cw_loginPwd})
                )
                # 校验 HTTP 状态码
                if result.status_code != 200:
                    raise ValueError(f"登录失败，状态码: {result.status_code}")
                # 解析 JSON
                response = result.json()
                if not response.get('success'):
                    raise ValueError(f"业务逻辑失败: {response}")
                # 提取 Token
                cls._cw_token = response['data']
                # print(f"[INFO] Token 已缓存: {cls._bm_token}")
            except Exception as e:
                print(f"[ERROR] 获取 Token 失败: {str(e)}")
                cls._cw_token = None  # 清除缓存以便重试
        return cls._cw_token

    @classmethod
    def lg_artifact_admin_token(cls):
        """
            获取物流神器admin登录的token
            :return:
        """
        if cls._admin_token is None:
            try:
                s = Base()
                result = s.requests_type(
                    method='POST',
                    url=config.admin_host+ '/api/loginByName',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps({"loginName": config.admin_loginName, "loginPwd": config.admin_loginPwd})
                )

                # 校验 HTTP 状态码
                if result.status_code != 200:
                    raise ValueError(f"登录失败，状态码: {result.status_code}")

                # 解析 JSON
                response = result.json()
                if not response.get('success'):
                    raise ValueError(f"业务逻辑失败: {response}")

                # 提取 Token
                cls._admin_token = response['data']
                #print(f"[INFO] Token 已缓存: {cls._bm_token}")
                return cls._admin_token
            except Exception as e:
                print(f"[ERROR] 获取 Token 失败: {str(e)}")
                cls._admin_token = None
        return cls._admin_token

    @classmethod
    def lg_bm_token(cls):
        """
            获取物流神器-5.0登录的token
            :return:
        """
        if cls._bm_token is None:
            try:
                s = Base()
                result = s.requests_type(
                    method='POST',
                    url= config.bm_host+'/api/login/loginByAccount',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps({"mobile":config.bm_mobile,"loginPwd":config.bm_loginPwd})
                )

                # 检查 HTTP 状态码
                if result.status_code != 200:
                    raise ValueError(f"HTTP 状态码异常: {result.status_code}")

                # 解析JSON
                response = result.json()
                if not response.get('success'):
                    raise ValueError(f"业务逻辑失败: {response}")

                # 提取 Token
                cls._bm_token = response['data']
                #print(f"[INFO] Token 已缓存: {cls._bm_token}")
            except Exception as e:
                #print(f"[ERROR] 获取 Token 失败: {str(e)}")
                cls._bm_token = None
        return cls._bm_token



