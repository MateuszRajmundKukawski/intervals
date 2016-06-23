import re
import unittest

def split_list(_str):
    pattern = '\s|,|;|:'
    splited_list = re.split(pattern, _str.strip())
    splited_list_int = [int(x) for x in splited_list if x]
    return splited_list_int


class TestLoclaFunc(unittest.TestCase):
    def test_split_list(self):
        tested_string = '12 12 12'
        expected_list = [12, 12, 12]
        result_list = split_list(tested_string)
        self.assertEqual(expected_list, result_list)
        tested_string = ' 12 12 12 '
        expected_list = [12, 12, 12]
        result_list = split_list(tested_string)
        self.assertEqual(expected_list, result_list)
        tested_string = '12  12 12'
        expected_list = [12, 12, 12]
        result_list = split_list(tested_string)
        self.assertEqual(expected_list, result_list)

        tested_string = '12  12 12'
        expected_list = [12, 12, 12]
        result_list = split_list(tested_string)
        self.assertEqual(expected_list, result_list)

        tested_string = '12; 12 12'
        expected_list = [12, 12, 12]
        result_list = split_list(tested_string)
        self.assertEqual(expected_list, result_list)

        tested_string = '12 : 12,12'
        expected_list = [12, 12, 12]
        result_list = split_list(tested_string)
        self.assertEqual(expected_list, result_list)

        tested_string = '12, 12 12'
        expected_list = [12, 12, 12]
        result_list = split_list(tested_string)
        self.assertEqual(expected_list, result_list)

        tested_string = '12\t12 12'
        expected_list = [12, 12, 12]
        result_list = split_list(tested_string)
        self.assertEqual(expected_list, result_list)

if __name__ == "__main__":
    unittest.main()