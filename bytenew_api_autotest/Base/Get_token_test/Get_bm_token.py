import hashlib
import json
from Base.Base_Page import Base

class Get_token():
    _bm_token = None

    @classmethod
    def lg_bm_pre_token(cls):
        """
            获取物流神器-5.0登录的Cookie
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
                print(f"[INFO] Token 已缓存: {cls._bm_token}")
            except Exception as e:
                print(f"[ERROR] 获取 Token 失败: {str(e)}")
                cls._bm_token = None
        return cls._bm_token