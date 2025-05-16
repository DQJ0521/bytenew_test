import unittest
from pathlib import Path
import unittestreport
from unittestreport import TestRunner
import common.commons as common

if __name__ == '__main__':
    #suite = unittest.defaultTestLoader.discover(r'cases_inspection')

    # 获取cases_inspection的绝对路径
    cases_dir = Path(__file__).parent / "cases_apicheck"
    cases_dir = cases_dir.resolve()  # 确保路径标准化

    # 发现所有测试用例（递归子目录）
    suite = unittest.defaultTestLoader.discover(
        start_dir=str(cases_dir),  # 起始目录
        pattern="test*.py",  # 匹配所有以test开头的py文件
        top_level_dir=None  # 确保递归所有子目录
    )
    # 生成报告
    reporter = common.Common()
    report_path = reporter.generate_html_report(suite,title="接口巡检测试报告")
    if report_path:
        print(f"查看报告: file://{report_path}")

    else:
        print("报告生成失败，请检查日志")


