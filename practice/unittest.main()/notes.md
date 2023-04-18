# Understand :if __name__ == ‘__main__‘: unittest.main()
## unittest是python自带的单元测试框架，有时候被称为"PyUnit".
### 在学习使用unittest库之前，我们需要了解一下unittest库的一些重要概念:
test fixture:
代表了用例执行前的准备工作和用例执行之后的清理工作。比如在用例执行前创建临时文件和文件夹，又或者启动1个server进程等；

test case:
测试用例，这个相信大家都不陌生。是测试的最小单位，一般检查一组输入的响应(输出)是否符合预期。unittest模块提供了TestCase类来帮助我们创建测试用例；

test suite:
经常被翻译成"测试套件"，也有人称为"测试套"，是测试用例或测试套件的集合，一般用来把需要一起执行的用例组合到一起;

test runner:
用来执行测试用例并输出测试结果的组件。可以是图形界面或命令行界面
基本用法举例
我们通过最简单的例子来看一下unittest的基本用法，下面的代码测试了3个python字符串方法，基本上满足了大部分情况下的测试需求。

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

为了理解‘if __name__ == '__main__':
    unittest.main()’，进行一下练习

1. __name__是python自带的属性，叫“内置名称”，不需要你定义，不需要你赋值，它的值是你【当前运行程序】的名称。
运行程序，只有两种情况：1.自己运行自己 2.被其他文件调用

1.自己运行自己，__name__值是__main__
（1）创建test1.py
 (2)unittest.main()
重点：这是做自动化、接口测试才会用到的东西，如果你只是开发就无需了解了。
unittest是单元测试框架，python自带的，拿来就能用。
unittest.main()运行开头为“test”的函数。
**代码如下：**
import unittest

class drink(unittest.TestCase):
    def test_xixi(self):
        print('我会运行！！！')
    def oh_no(self): # 不是以test开头的函数，不会被执行
        print('我不会运行')
        
if __name__ == '__main__':
    unittest.main()




