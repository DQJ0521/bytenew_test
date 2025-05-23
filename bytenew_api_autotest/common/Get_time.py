from datetime import datetime,timedelta
import json

class Get_time():
    @classmethod
    def now(cls):
        # 正确获取完整日期时间
        now = datetime.now()
        cls.now = now.strftime("%Y-%m-%d %H:%M:%S")

        return cls.now

    @classmethod
    def before_now(cls):
        # 获取当前时间并减 2 分钟
        now = datetime.now()
        adjusted_time = now - timedelta(minutes=2)
        cls.before_now = adjusted_time.strftime("%Y-%m-%d %H:%M:%S")
        return cls.before_now