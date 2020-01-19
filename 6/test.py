import unittest
import main

class TestMain(unittest.TestCase):
    def test_2(self):
        self.assertEqual(main.calc(["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"]), 42)
        self.assertEqual(main.calcAdv(["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L","K)YOU","I)SAN"]), 4)
if __name__ == "__main__":
    unittest.main()
