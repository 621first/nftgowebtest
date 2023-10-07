'''
@filename: /customErrorReporter
@time: 2023/10/7 14:18
'''
import pytest

class CustomErrorReporter(pytest.TestReport):

    def pytest_runtest_logreport(self, report):
        if report.failed:
            # 获取测试用例的错误信息
            error_msg = getattr(report.longrepr, 'reprcrash', '')
            # 将错误信息添加到测试报告中
            self.write_sep('=', 'ERROR DETAILS')
            self.write_line(error_msg)
