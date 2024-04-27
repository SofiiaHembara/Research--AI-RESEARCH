import unittest
from improved_code_gemini import create_table, flatten

class RecursiveFunctionsTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_table(self):
        expected_table = []
        self.assertEqual(create_table(0, 0), expected_table)

    def test_one_row_one_column(self):
        expected_table = [[1]]
        self.assertEqual(create_table(1, 1), expected_table)

    def test_one_row_multiple_columns(self):
        expected_table = [[1, 1, 1, 1, 1]]
        self.assertEqual(create_table(1, 5), expected_table)

    def test_multiple_rows_one_column(self):
        expected_table = [[1], [1], [1], [1], [1]]
        self.assertEqual(create_table(5, 1), expected_table)

    def test_multiple_rows_multiple_columns(self):
        expected_table = [
            [1, 1, 1, 1, 1, 1],
            [1, 2, 3, 4, 5, 6],
            [1, 3, 6, 10, 15, 21],
            [1, 4, 10, 20, 35, 56]
        ]
        self.assertEqual(create_table(4, 6), expected_table)

    def test_invalid_n_type(self):
        with self.assertRaises(TypeError):
            create_table('abc', 5)

    def test_invalid_m_type(self):
        with self.assertRaises(TypeError):
            create_table(4, 'abc')

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            create_table(-1, 5)

    def test_negative_m(self):
        with self.assertRaises(ValueError):
            create_table(4, -2)

    def test_flat_list(self):
        expected_list = [1, 2, 3]
        self.assertEqual(flatten([1, 2, 3]), expected_list)

    def test_nested_list_one_level(self):
        expected_list = [1, 2, 3]
        self.assertEqual(flatten([1, [2], 3]), expected_list)

    def test_nested_list_multiple_levels(self):
        expected_list = [1, 2, 3, 4, 5]
        self.assertEqual(flatten([1, [2, [3, 4]], 5]), expected_list)

    def test_empty_list(self):
        expected_list = []
        self.assertEqual(flatten([]), expected_list)

    def test_nested_empty_list(self):
        expected_list = []
        self.assertEqual(flatten([[], []]), expected_list)

    def test_string(self):
        expected_list = ['h', 'e', 'l', 'l', 'o']
        self.assertEqual(flatten('hello'), expected_list)

    def test_non_list_argument(self):
        self.assertEqual(flatten(1), 1)
    
    def test_negative_n_raises_value_error(self):
        with self.assertRaises(ValueError):
            create_table(-1, 5)

    def test_negative_m_raises_value_error(self):
        with self.assertRaises(ValueError):
            create_table(4, -2)

    def test_n_equals_1_and_m_equals_1(self):
        expected_table = [[1]]
        self.assertEqual(create_table(1, 1), expected_table)

    def test_flatten_with_string(self):
        expected_list = ['h', 'e', 'l', 'l', 'o']
        self.assertEqual(flatten('hello'), expected_list)

    def test_flatten_with_non_list_argument(self):
        self.assertEqual(flatten(1), 1)

#Оптимізовані тести
# import unittest
# from improved_code_gemini import create_table, flatten


# class RecursiveFunctionsTest(unittest.TestCase):

#     def test_empty_or_invalid_table_size(self):
#         # Combine multiple test cases for empty and invalid table sizes
#         with self.assertRaises(ValueError):
#             create_table(-1, 5)
#         with self.assertRaises(TypeError):
#             create_table('abc', 5)
#         with self.assertRaises(ValueError):
#             create_table(4, -2)
#         with self.assertRaises(TypeError):
#             create_table(4, 'abc')
#         self.assertEqual(create_table(0, 0), [])  # Test empty table

#     def test_one_dimension_table(self):
#         # Combine multiple test cases for one-dimensional tables
#         self.assertEqual(create_table(1, 1), [[1]])
#         self.assertEqual(create_table(5, 1), [[1], [1], [1], [1], [1]])

#     def test_multiple_dimension_table(self):
#         # Combine multiple test cases for multi-dimensional tables
#         expected_table = [
#             [1, 1, 1, 1, 1, 1],
#             [1, 2, 3, 4, 5, 6],
#             [1, 3, 6, 10, 15, 21],
#             [1, 4, 10, 20, 35, 56]
#         ]
#         self.assertEqual(create_table(4, 6), expected_table)

#     def test_flatten(self):
#         # Combine multiple test cases for flatten function
#         self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])
#         self.assertEqual(flatten([1, [2], 3]), [1, 2, 3])
#         self.assertEqual(flatten([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])
#         self.assertEqual(flatten([]), [])
#         self.assertEqual(flatten([[], []]), [])
#         self.assertEqual(flatten('hello'), ['h', 'e', 'l', 'l', 'o'])
#         self.assertEqual(flatten(1), 1)

# if __name__ == '__main__':
#     unittest.main()