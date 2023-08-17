import unittest
from ThreeSum import Solution

class TestSolution(unittest.TestCase):
    def test_threeSum(self):
        sol = Solution()
        nums = [-1,0,1,2,-1,-4]
        expected_output = [[-1,-1,2],[-1,0,1]]

        # Ensure the function returns the expected output
        self.assertEqual(sol.threeSum(nums), expected_output)

        # Ensure the function returns empty list if no triplet found
        self.assertEqual(sol.threeSum([]), [])

        # Ensure the function works with duplicate values
        nums = [-1,0,1,1,1,2,-1,-4]
        expected_output = [[-1,-1,2],[-1,0,1]]

        self.assertEqual(sol.threeSum(nums), expected_output)

if __name__ == '__main__':
    unittest.main()
