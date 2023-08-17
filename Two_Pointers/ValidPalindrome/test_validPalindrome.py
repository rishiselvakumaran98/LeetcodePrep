import unittest
from ValidPalindrome import Solution

class TestSolution(unittest.TestCase):
    def test_isPalindrome(self):
        # test cases for when s is a palindrome
        sol = Solution()
        self.assertEqual(sol.isPalindrome("A man a plan a canal Panama"), True)
        self.assertEqual(sol.isPalindrome("race car"), True)
        self.assertEqual(sol.isPalindrome("Was It A Rat I Saw?"), True)
        self.assertEqual(sol.isPalindrome("A Santa Lived As a Devil At NASA"), True)
        
        # test cases for when s is not a palindrome
        self.assertEqual(sol.isPalindrome("hello world"), False)
        self.assertEqual(sol.isPalindrome("12321r"), False)
        
        # test an empty string
        self.assertEqual(sol.isPalindrome(""), True)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
