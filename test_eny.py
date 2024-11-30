import unittest
from app import add, multi, division

class Tests(unittest.TestCase):
    def testmy(self):
        self.assertEqual(multi(2, 3), 6)
        # self.assertEqual(multi(2, 3), 5)
        self.assertEqual(multi(1, 3), 3)
        self.assertEqual(add(0, 0), 2)
        self.assertEqual(division(6,2),3)
        self.assertEqual(division(0,3),0)
        self.assertEqual(division(3,0),0)

if __name__ == '__main__':
    unittest.main()
