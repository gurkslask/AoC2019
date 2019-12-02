import unittest
import main

class TestMain(unittest.TestCase):
    def test_2(self):
        self.assertEqual(main.calc("1,0,0,0,99"), 2)
        self.assertEqual(main.calc("1,1,1,4,99,5,6,0,99"), 30)

if __name__ == "__main__":
    unittest.main()
