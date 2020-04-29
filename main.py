import os
import HTMLTestRunner
from BeautifulReport import BeautifulReport

from Common.dir_config import *
import unittest
from TestCase.test_login import TestLogin

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestLogin))

# with open(htmlreport_dir+"/autoTest_report.html","wb") as fp:
result = BeautifulReport(suite)
result.report(filename='测试报告', description='测试deafult报告', log_path=htmlreport_dir)
#     runner.run(suite)


