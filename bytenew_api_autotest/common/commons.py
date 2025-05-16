import logging,time
import os
from typing import Optional

import pandas as pd
from logging.handlers import TimedRotatingFileHandler
from unittestreport import TestRunner
#from HTMLTestReportCN import HTMLTestRunner
from pathlib import Path
import unittest


base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
log_path = os.path.join(base_path, 'report', 'logs')
report_html = os.path.join(base_path, 'report', 'html')
read_xlrd = os.path.join(base_path, 'data')

class Common():
    #封装日志方法
    _logs_initialized = False # 确保日志只初始化一次
    def get_logs(self,path = log_path):
        # 确保路径存在
        os.makedirs(path,exist_ok=True)

        # 获取日志器（命名为当前类名）
        logger = logging.getLogger(self.__class__.__name__)
        if Common._logs_initialized:
            return logger  # 避免重复配置

        logger.setLevel(logging.DEBUG)

        # 1. 文件处理器：按天滚动生成日志文件
        log_file = os.path.join(path,f"{time.strftime('%Y-%m-%d')}.log")
        file_handler = TimedRotatingFileHandler(
            filename=log_file,
            when='midnight',  # 每天午夜滚动
            backupCount=7,  # 保留最近7天日志
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)

        # 2. 控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # 统一日志格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 添加处理器
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        Common._logs_initialized = True
        return logger

# 读取Excel表方法，方便后续读取接口用例数据
    def ReadExcelTypeDict(self,file_name,path = read_xlrd):
        # 安全拼接文件路径
        full_path = os.path.join(path,file_name)
        print(f"完整文件路径:{full_path}")

        try:
            excel_file = pd.ExcelFile(full_path,engine="openpyxl")
        except Exception as e:
            print(f"读取 Excel 失败:{e}")
            return []

        # 遍历所有 Sheet 并读取数据
        new_list = []
        for sheet_name in excel_file.sheet_names:
            # 指定第一行为标题行（header=0）
            df = pd.read_excel(excel_file,sheet_name = sheet_name,header=0)

            # 转换为字典列表（自动处理标题与数据的映射）
            sheet_data = df.to_dict('records')
            new_list.extend(sheet_data)

        return new_list

    def ReadExcelTypeDict_sliced(self, file_name, path=read_xlrd, start_row=0, end_row=None):
        """
        读取 Excel 数据并转换为字典列表（支持指定行数范围）

        :param file_name: 文件名
        :param path: 文件路径（默认读取配置中的路径）
        :param start_row: 起始行号 (从0开始, 默认0)
        :param end_row: 结束行号 (不包含此行, 默认None表示最后一行)
        :return: 字典列表
        """
        full_path = os.path.join(path, file_name)
        print(f"完整文件路径: {full_path}")

        try:
            excel_file = pd.ExcelFile(full_path, engine="openpyxl")
        except Exception as e:
            print(f"读取 Excel 失败: {e}")
            return []

        new_list = []
        for sheet_name in excel_file.sheet_names:
            # 读取整个Sheet
            df = pd.read_excel(excel_file, sheet_name=sheet_name, header=0)

            # 切片指定行数（处理边界）
            max_row = len(df)
            _end_row = end_row if end_row is not None else max_row
            _end_row = min(_end_row, max_row)  # 避免越界

            sliced_df = df.iloc[start_row:_end_row]

            # 转换为字典
            sheet_data = sliced_df.to_dict('records')
            new_list.extend(sheet_data)
            print(f"Sheet [{sheet_name}] 读取行范围: {start_row}-{_end_row}, 实际行数: {len(sheet_data)}")

        return new_list

# 封装一个HTML报告方法
    def generate_html_report(self, suite: unittest.TestSuite, title: str, report_dir: str=report_html) -> Optional[
        str]:
        """
        生成HTML测试报告
        """
        try:
            # 创建报告目录
            project_root = Path(__file__).parent.parent.absolute()
            output_dir = project_root / report_dir
            os.makedirs(output_dir, exist_ok=True)

            # 生成报告文件名
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"{title}_{timestamp}.html"
            report_path = output_dir / filename

            # 初始化TestRunner并运行测试
            runner = TestRunner(
                suite=suite,
                filename=str(report_path),
                report_dir=str(output_dir),
                title=title,
                tester="自动化测试团队",
                desc="接口自动化测试报告",
                templates=1
            )
            runner.run()

            # #发送结果到邮箱
            '''
            host： smtp服务器地址
            port：端口
            user：邮箱账号
            password：smtp服务授权码
            to_addrs：收件人邮箱地址（一个收件人传字符串，多个收件人传列表）
            注意：目前发送邮件只支持465和25端口
            '''
            # runner.send_email(
            #     host="smtp.qq.com",
            #     port=465,
            #     user="",
            #     password="",
            #     to_addrs=""
            # )

            # #发送钉钉通知
            # url = "https://oapi.dingtalk.com/robot/send?access_token=80777bc3b2be980c46dc5fcaeac5afff7aabf91c8cb59f55b4cc76fbc272f585"
            # runner.dingtalk_notice(url=url,secret="SEC5059b41b3699f5714a217a38b9af49e67cb58659035e053214b07d1a5c00c162")

            return str(report_path)

        except Exception as e:
            print(f"报告生成失败: {str(e)}")
            return None

