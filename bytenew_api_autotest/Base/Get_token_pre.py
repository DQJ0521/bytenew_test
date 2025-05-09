#_*_encoding:utf-8_*_
import hashlib
import unittest
from Base.Base_Page import Base
import json

class Get_token():
    # 类属性缓存不同服务的 Token
    _cw_token = None
    _admin_token = None
    _artifact_token = None
    _bm_token = None

    @classmethod
    def lg_cw_pre_token(cls):
        """
            获取云仓登录的token
            :return:
        """
        if cls._cw_token is None:
            try:
                s = Base()
                result = s.requests_type(
                    method='POST',
                    url='https://lg-cw-pre.bytenew.com/api/user/normalUserLogin',
                    headers={'lg-cw-client': '1', 'Content-Type': 'application/json'},
                    data=json.dumps({"loginPwd": "YC888888", "mobile": "13588888888"})
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
    def lg_artifact_admin_pre_token(cls):
        """
            获取物流神器admin登录的token
            :return:
        """
        if cls._admin_token is None:
            try:
                s = Base()
                result = s.requests_type(
                    method='POST',
                    url='https://lg-artifact-admin-pre.bytenew.com/api/loginByName',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps({"loginName": "admin", "loginPwd": "lg123456"})
                )

                # 校验 HTTP 状态码
                if result.status_code != 200:
                    raise ValueError(f"登录失败，状态码: {result.status_code}")

                # 解析 JSON
                response = result.json()
                if not response.get('success'):
                    raise ValueError(f"业务逻辑失败: {response.get('errorMessage')}")

                # 提取 Token
                cls._admin_token = response['data']
                #print(f"[INFO] Token 已缓存: {cls._bm_token}")
                return cls._admin_token
            except Exception as e:
                print(f"[ERROR] 获取 Token 失败: {str(e)}")
                cls._admin_token = None
        return cls._admin_token

    @classmethod
    def lg_bm_pre_token(cls):
        """
            获取物流神器-5.0登录的token
            :return:
        """
        if cls._bm_token is None:
            try:
                s = Base()
                result = s.requests_type(
                    method='POST',
                    url='https://lg-bm-login-pre.bytenew.com/api/login/loginByAccount',
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps({"mobile":"19855555555","loginPwd":"555555"})
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



