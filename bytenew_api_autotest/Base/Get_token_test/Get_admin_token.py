import hashlib
import unittest
from Base.Base_Page import Base
import json
import common.commons as common

class Get_token():
    _admin_token = None
    @classmethod
    def lg_artifact_admin_pre_token(cls):
        if cls._admin_token is None:
            try:
                s = Base()
                url = 'https://lg-artifact-admin-pre.bytenew.com/api/loginByName'
                headers = {'Content-Type': 'application/json'}
                #hashed_pwd = hashlib.md5(password.encode()).hexdigest()
                data = json.dumps({"loginName": "admin", "loginPwd": "lg123456"})

                # 发送请求
                result = s.requests_type(
                    method='POST',
                    url=url,
                    headers=headers,
                    data=data
                )

                # 打印响应信息
                # print(f"[DEBUG] 响应状态码: {result.status_code}")
                # print(f"[DEBUG] 响应内容: {result.text}")

                # 校验 HTTP 状态码
                if result.status_code != 200:
                    raise ValueError(f"HTTP 状态码异常: {result.status_code}")

                # 解析 JSON
                response = result.json()
                if not response.get('success'):
                    error_msg = response.get('errorMessage', '未知错误')
                    raise ValueError(f"业务错误: {error_msg}")

                # 提取 Token
                cls._admin_token = response['data']
                print(f"[INFO] Token 已缓存: {cls._admin_token}")
                return cls._admin_token
            except json.JSONDecodeError:
                print("[ERROR] 响应不是有效的 JSON 格式")
                cls._admin_token = None
            except KeyError as e:
                print(f"[ERROR] 响应缺少关键字段: {str(e)}")
                cls._admin_token = None
            except Exception as e:
                print(f"[ERROR] 未知错误: {str(e)}")
                cls._admin_token = None
        return cls._admin_token
