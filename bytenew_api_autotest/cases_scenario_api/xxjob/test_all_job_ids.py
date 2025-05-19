#_*_encoding:utf-8_*_
import json
import unittest
from Base.Base_Page import Base
from Base.Get_xxjob_token import Get_token
import common.commons as commons
import config.config as config
from common.data_extractor import extract_nested_ids


class MyTestCase(unittest.TestCase):
    # 类变量用于缓存Group_ids
    _cached_group_ids = None
    @classmethod
    def setUpClass(cls):
        cls.logs = commons.Common().get_logs()
        cls.xxjob_pre_token = Get_token.lg_xxjob_pre_token()
        if cls._cached_group_ids is None:
            cls._cached_group_ids = []

    def test_1_jobgroup_pageList(self):
        '''
            获取所有定时任务的群组id
        '''
        if self.__class__._cached_group_ids is None:
            return self.__class__._cached_group_ids

       # length的总长度是102
        url = config.xxjob_host + "/jobgroup/pageList?appname&title&start=0&length=4"
        header = {'Content-Type': 'application/json', "Cookie": self.xxjob_pre_token}
        method = 'POST'
        result = Base().requests_type(method=method, url=url, headers=header)

        try:
            if result.status_code !=200:
                raise ValueError(f"请求失败，状态码: {result.status_code}")
            data_list = json.loads(result.text)
            # 提取特定键值
            self.__class__._cached_group_ids = extract_nested_ids(data_list, key='id')
            self.logs.info(f"所有定时任务Group_ID: {self.__class__._cached_group_ids}")

        except Exception as e:
            print(f"[ERROR] 获取 Group_id 失败: {str(e)}")

        return self.__class__._cached_group_ids

    def test_2_jobids(self):
        '''
            获取所有定时任务id
        '''

        all_job_ids = []

        if not self.__class__._cached_group_ids:
            self.test_1_jobgroup_pageList()

        for group_id in self.__class__._cached_group_ids:
            url = config.xxjob_host+"/jobinfo/pageList"
            header = {'Content-Type': 'application/x-www-form-urlencoded', "Cookie": self.xxjob_pre_token}
            method = 'POST'
            datas = {"jobGroup": group_id,"triggerStatus":"-1","start":"0","length":"10"}
            result = Base().requests_type(method=method, url=url, headers=header,data=datas)

            try:
                if result.status_code !=200:
                    raise ValueError(f"请求失败，状态码: {result.status_code}")
                ids_list = json.loads(result.text)
            # 提取特定键值
                all_ids = extract_nested_ids(ids_list, key='id')
                all_job_ids.extend(all_ids)

            except Exception as e:
                print(f"[ERROR] 获取 id 失败: {str(e)}")
        self.logs.info(f"所有定时任务ID的合集: {all_job_ids}")
        self.__class__._cached_joc_ids = all_job_ids
        return all_job_ids

if __name__ == '__main__':
    unittest.main()
