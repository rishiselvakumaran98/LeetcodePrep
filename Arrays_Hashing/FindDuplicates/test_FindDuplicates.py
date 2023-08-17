import unittest
from FindDuplicates import Solution

class TestSolution(unittest.TestCase):
    def test_findDuplicate_Neg_Marking(self):
        solution = Solution()

        self.assertEqual(solution.findDuplicate_Neg_Marking([1,3,4,2,2]), 2)
        self.assertEqual(solution.findDuplicate_Neg_Marking([3,1,3,4,2]), 3)
        self.assertEqual(solution.findDuplicate_Neg_Marking([1,1]), 1)
        self.assertEqual(solution.findDuplicate_Neg_Marking([1,1,2]), 1)

    def test_findDuplicate_Find_Cycle(self):
        solution = Solution()

        self.assertEqual(solution.findDuplicate_Find_Cycle([1,3,4,2,2]), 2)
        self.assertEqual(solution.findDuplicate_Find_Cycle([3,1,3,4,2]), 3)
        self.assertEqual(solution.findDuplicate_Find_Cycle([1,1]), 1)
        self.assertEqual(solution.findDuplicate_Find_Cycle([1,1,2]), 1)

if __name__ == '__main__':
    unittest.main()
