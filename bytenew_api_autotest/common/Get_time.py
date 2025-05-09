from datetime import datetime,timedelta
import json

class Get_time():
    def now(self):
        # 正确获取完整日期时间
        now = datetime.now()
        self.formatted = now.strftime("%Y-%m-%d %H:%M:%S")

        return self.formatted

    def before_now(self):
        # 获取当前时间并减 1 分钟
        now = datetime.now()
        adjusted_time = now - timedelta(minutes=2)
        self.before_now = adjusted_time.strftime("%Y-%m-%d %H:%M:%S")
        return self.before_now