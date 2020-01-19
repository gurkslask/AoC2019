import unittest
import main

class TestMain(unittest.TestCase):
    def test_2(self):
        # self.assertEqual(main.calc("10101,2,1,0,99"), 4)
        # self.assertEqual(main.calc("11101,4,4,0,99"), 8)
        # self.assertEqual(main.calc("10001,2,1,0,99"), 3)
        # self.assertEqual(main.calc("10002,2,1,0,99"), 2)
        # self.assertEqual(main.calc("11102,8,5,0,99"), 40)
        # self.assertEqual(main.calc("103,2,9,0,1,3,99"), 105)
        print("test1")
        self.assertEqual(main.calc("3,9,8,9,10,9,4,9,99,-1,8", 8), 1)
        print("test2")
        self.assertEqual(main.calc("3,9,8,9,10,9,4,9,99,-1,8", 7), 0)
        print("test3")
        self.assertEqual(main.calc("3,9,7,9,10,9,4,9,99,-1,8", 7), 1)
        print("test4")
        self.assertEqual(main.calc("3,9,7,9,10,9,4,9,99,-1,8", 19), 0)
        print("test5")
        self.assertEqual(main.calc("3,3,1108,-1,8,3,4,3,99", 19), 0)
        print("test6")
        self.assertEqual(main.calc("3,3,1108,-1,8,3,4,3,99", 8), 1)
        print("test7")
        self.assertEqual(main.calc("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 0), 0)
        print("test8")
        self.assertEqual(main.calc("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", 5), 1)
        print("test9")
        self.assertEqual(main.calc("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", 0), 0)
        print("test10")
        self.assertEqual(main.calc("3,3,1105,-1,9,1101,0,0,12,4,12,99,1", 5), 1)
        print("test11")
        self.assertEqual(main.calc("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", 5), 999)

if __name__ == "__main__":
    unittest.main()
