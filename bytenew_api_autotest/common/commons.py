import logging,time
import os

import pandas as pd
from logging.handlers import TimedRotatingFileHandler
from HTMLTestReportCN import HTMLTestRunner
from pathlib import Path


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


# 封装一个HTML报告方法
    def GetHtmlResult(self, suite, title, path='test_reports'):
        try:
            # 路径：指向项目根目录
            project_root = Path(__file__).parent.parent.absolute()
            report_dir = project_root / path
            os.makedirs(report_dir, exist_ok=True)

            report_name = f"{title}_{time.strftime('%Y-%m-%d-%H-%M-%S')}.html"
            report_path = report_dir / report_name

            with open(report_path, 'wb') as f:
                runner = HTMLTestRunner(
                    stream=f, title=title, description='接口测试报告', tester='哈比'
                )
                result = runner.run(suite)
                self.get_logs().info(f"执行用例数: {result.testsRun}, 失败: {len(result.failures)}")

            self.get_logs().info(f"报告路径: {report_path}")
            return str(report_path)
        except Exception as e:
            self.get_logs().error(f"生成报告失败: {str(e)}", exc_info=True)
            return None
#     def GetHtmlResult(self,suite,title,path = 'test_reports'):
#
#         project_root = Path(__file__).parent.absolute()
#         report_dir = project_root/path
#         os.makedirs(report_dir,exist_ok=True)
#         print(f"报告目录：{report_dir}")
#
#         report_name =f"{title}_{time.strftime('%Y-%m-%d-%H-%M-%S')}.html"
#         report_path = report_dir/report_name
#         #report_path = os.path.join(path,report_name)
#
#         try:
#             with open(report_path, 'wb') as f:
#                 runner = HTMLTestRunner(
#                     stream=f, description='用户相关接口测试报告', tester='哈比', title=title
#                 )
#                 result = runner.run(suite)
#                 print(f"测试结果: {result.testsRun} 条用例执行，失败 {len(result.failures)} 条")
#             print(f"报告已生成: {report_path}")
#             return str(report_path)
#         except Exception as e:
#             print(f"生成报告异常: {str(e)}")
#             return None
#
#         # path = path + '/' + time.strftime('%Y-%m-%d-%H-%M-%S') + '.html'
#         # with open(path,'wb+') as f:
#         #     run = HTMLTestReportCN.HTMLTestRunner(stream=f,description='用户相关接口测试报告',tester='哈比',title = title)
#         #     run.run(suite)

