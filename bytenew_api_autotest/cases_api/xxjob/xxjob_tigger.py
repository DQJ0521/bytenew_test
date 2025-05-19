#_*_encoding:utf-8_*_
from Base.Base_Page import Base
from Base.Get_xxjob_token import Get_token
import common.commons as commons
import config.config as config

class xxjob_tigger():
    '''
    xxjob任务执行 接口，给到其他case调用，调用时根据需求修改jobid
    '''
    _xxjob_token = None

    # @classmethod
    # def setUpClass(cls):
    #     cls.logs = commons.Common().get_logs()
    #     cls.xxjob_pre_token = Get_token.lg_xxjob_pre_token()
    #     cls.logs.info(f"获取到的token：{cls.xxjob_pre_token}")

    # def xxjob_excute(self,job_id):
    #
    #     url = config.xxjob_host+"/jobinfo/trigger"
    #     header = {'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': self.xxjob_pre_token}
    #     method = 'POST'
    #     datas = {"id":{job_id},"executorParam":"","addressList":""}
    #     result = Base().requests_type(method=method, url=url, headers=header,data=datas)
    #     self.logs.info(f"请求数据：{result.request.body}")
    #     self.logs.info(f"响应结果：{result.text}")
    #
    #     #assert result.status_code == 200
    #     #self.assertEqual(result.status_code,200,"接口执行失败")
    #     return result

    """
    XXJob定时任务触发工具类
    使用示例：
    result = XXJobOperator.trigger_job(job_id='355')
    """
    #_token = None  # 类变量缓存token

    @classmethod
    def _init_token(cls):
        """确保token只初始化一次"""
        if not cls._xxjob_token:
            cls._xxjob_token = Get_token.lg_xxjob_pre_token()
            commons.Common().get_logs().info(f"XXJob Token已初始化")

    @classmethod
    def trigger_job(cls, job_id: str) -> dict:
        """
        触发指定任务
        :param job_id: 任务ID
        :return: 接口响应结果
        """
        # 确保token已初始化
        cls._init_token()

        # 构建请求参数
        url = f"{config.xxjob_host}/jobinfo/trigger"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cls._xxjob_token
        }
        data = {"id": job_id, "executorParam": "", "addressList": ""}

        # 发送请求
        result = Base().requests_type(
            method='POST',
            url=url,
            headers=headers,
            data=data
        )

        # 记录日志
        commons.Common().get_logs().info(
            f"任务触发请求:\nURL: {url}\n请求体: {data}\n响应状态: {result.status_code}\n响应内容: {result.text[:200]}..."
        )

        return result.json()