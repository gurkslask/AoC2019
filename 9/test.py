import unittest
import main

class TestMain(unittest.TestCase):
    def test_2(self):
        print("test1")
        self.assertEqual(main.calc("104,1125899906842624,99", 0, 0), 1125899906842624)
        self.assertEqual(main.calc("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99", 0, 0), 109)
        self.assertEqual(len(str(abs(main.calc("1102,34915192,34915192,7,4,7,99,0", 0, 0)))), 16)
        print("test2")


if __name__ == "__main__":
    unittest.main()
