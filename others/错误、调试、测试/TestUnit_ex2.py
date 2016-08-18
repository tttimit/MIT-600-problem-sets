"""
单元测试的测试文件
"""

import unittest
from TestUnit_ex import Dict

class TestDict(unittest.TestCase):
    #有test前缀的方法才是测试方法，没有的话测试时不会执行
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    ## setUp() 和 tearDown() 在调用每个测试方法前后调用，例如打开/关闭数据库
    def setUp(self):
        print("setup...")

    def tearDown(self):
        print("teardown...")

if __name__ == '__main__':
    unittest.main()
