import unittest
import unittestreport
from unittestreport import TestRunner
import common.commons as common

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover(r'cases_inspection/lg_cw')
    # 生成报告
    reporter = common.Common()
    report_path = reporter.generate_html_report(suite,
        title="班门接口巡检测试报告"
    )
    if report_path:
        print(f"查看报告: file://{report_path}")

    else:
        print("报告生成失败，请检查日志")


