import unittest
from typing import List
from Encode_Decode import Codec

class TestCodec(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def test_encode(self):
        # test case 1
        input_strs = ["Hello", "World"]
        expected_output = "5/Hello5/World"
        self.assertEqual(self.codec.encode(input_strs), expected_output)

        # test case 2
        input_strs = ["Hello", "", "World"]
        expected_output = "5/Hello0/5/World"
        self.assertEqual(self.codec.encode(input_strs), expected_output)

        # test case 3
        input_strs = []
        expected_output = ""
        self.assertEqual(self.codec.encode(input_strs), expected_output)

    def test_decode(self):
        # test case 1
        input_str = "5/Hello5/World"
        expected_output = ["Hello", "World"]
        self.assertEqual(self.codec.decode(input_str), expected_output)

        # test case 2
        input_str = "5/Hello0/5/World"
        expected_output = ["Hello", "", "World"]
        self.assertEqual(self.codec.decode(input_str), expected_output)

        # test case 3
        input_str = ""
        expected_output = []
        self.assertEqual(self.codec.decode(input_str), expected_output)

if __name__ == '__main__':
    unittest.main()
