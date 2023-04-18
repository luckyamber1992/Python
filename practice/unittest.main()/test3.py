import unittest
class drink(unittest.TestCase):
    def test_xixji(self):
        print('我会运行！！！')
    def est_no(self): # 不是以test开头的函数，不会被执行
        print('我不会运行')
        
if __name__ == '__main__':
    unittest.main()

