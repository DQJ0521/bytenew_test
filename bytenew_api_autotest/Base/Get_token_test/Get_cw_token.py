import hashlib
import json
from Base.Base_Page import Base
import config.config as config

class Get_token():
    """
        获取云仓登录的token
        :return:
    """
    _cw_token = None

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
                    url=config.cw_host + '/api/user/normalUserLogin',
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
                print(f"[INFO] Token 已缓存: {cls._cw_token}")
            except Exception as e:
                print(f"[ERROR] 获取 Token 失败: {str(e)}")
                cls._cw_token = None  # 清除缓存以便重试
        return cls._cw_token