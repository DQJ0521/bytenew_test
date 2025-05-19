class JobConfig:
    # 使用类变量存储任务映射，便于统一维护
    SOURCE_TO_JOB_ID = {
        '1': '362',    # 淘宝
        '8': '1367',   # 天猫
        '37': '355',   # 抖音
        '3': '357',    # 京东
        '36': '496',   # 快手
        '29': '360'    # 拼多多
    }

    @classmethod
    def get_job_id(cls, source: str) -> str:
        """
        根据业务来源获取对应的定时任务ID
        :param source: 业务来源标识 (如 '1' 代表淘宝)
        :return: 任务ID字符串
        :raises ValueError: 当传入无效来源时抛出
        """
        job_id = cls.SOURCE_TO_JOB_ID.get(str(source))
        if not job_id:
            raise ValueError(f"无效业务来源标识: {source}，支持来源: {list(cls.SOURCE_TO_JOB_ID.keys())}")
        return job_id

    @classmethod
    def get_all_sources(cls) -> dict:
        """获取完整的来源映射关系 (只读)"""
        return cls.SOURCE_TO_JOB_ID.copy()