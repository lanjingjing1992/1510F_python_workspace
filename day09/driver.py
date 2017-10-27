#coding= utf-8
from unit.Widget import *
import time
import unittest
# 执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def testLogin(self):
        print 'abc'
    def tearDown(self):
        pass
    #构造测试集
    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(WidgetTestCase("testLogin"))
        return suite

    # 测试
    if __name__ == "__main__":
        unittest.main(defaultTest='suite')