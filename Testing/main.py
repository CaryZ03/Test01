import unittest

from White import Triangle
from Black import CheckId


class MyTest(unittest.TestCase):
    # 编写测试用例，记得要以t开头，例：test
    def testEqual(self):
        # 调用内部的测试方法，如：assertEqual,assertNotEqual 等
        self.assertEqual(Triangle.triangle(3, 4, 5), "regular triangle!")

    def testNotEqual(self):
        self.assertEqual(Triangle.triangle("3", 4, 5), "not a triangle!")

    def testId(self):
        # Black 传入身份证号，调用 exec 返回验证的结果
        self.assertEqual(CheckId.Black('110221201813010003').exec(), 1)
        pass

# 运行测试
if __name__ == '__main__':
    unittest.main()
