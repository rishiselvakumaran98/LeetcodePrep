import unittest
from ContainsDuplicate import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_containsDuplicate(self):
        self.assertEqual(self.obj.containsDuplicate([1,2,3,4,5]), False)
        self.assertEqual(self.obj.containsDuplicate([1,2,3,4,5,1]), True)
        self.assertEqual(self.obj.containsDuplicate([1,1,1,1,1,1]), True)
        self.assertEqual(self.obj.containsDuplicate([1,2,3,4,5,6,7]), False)
        self.assertEqual(self.obj.containsDuplicate([1,2,3,4,5,6,7,7]), True)

if __name__ == '__main__':
    unittest.main()
