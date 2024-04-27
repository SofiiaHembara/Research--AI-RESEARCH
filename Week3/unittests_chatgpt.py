# import unittest
# from initial_code import create_table, flatten

# class TestCreateTable(unittest.TestCase):
#     def test_create_table_4_6(self):
#         self.assertEqual(create_table(4, 6), [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]])

#     def test_create_table_1_1(self):
#         self.assertEqual(create_table(1, 1), [[1]])

#     def test_create_table_0_5(self):
#         self.assertEqual(create_table(0, 5), [])

#     def test_create_table_5_0(self):
#         self.assertEqual(create_table(5, 0), [])

#     def test_create_table_2_3(self):
#         self.assertEqual(create_table(2, 3), [[1, 1, 1], [1, 2, 3]])
# class TestFlatten(unittest.TestCase):
#     def test_flatten_1(self):
#         self.assertEqual(flatten([1, [2]]), [1, 2])

#     def test_flatten_2(self):
#         self.assertEqual(flatten([1, 2, [3, [4, 5], 6], 7]), [1, 2, 3, 4, 5, 6, 7])

#     def test_flatten_3(self):
#         self.assertEqual(flatten(['wow', [2, [[]]], [True]]), ['wow', 2, True])

#     def test_flatten_4(self):
#         self.assertEqual(flatten([]), [])

#     def test_flatten_5(self):
#         self.assertEqual(flatten([[]]), [])

#     def test_flatten_6(self):
#         self.assertEqual(flatten(3), 3)

# if __name__ == '__main__':
#     unittest.main()

import unittest
from improved_code_chatgpt import create_table, flatten

class TestCreateTable(unittest.TestCase):
    def test_create_table_4_6(self):
        self.assertEqual(create_table(4, 6), [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]])

    def test_create_table_1_1(self):
        self.assertEqual(create_table(1, 1), [[1]])

    def test_create_table_0_5(self):
        self.assertEqual(create_table(0, 5), [])

    def test_create_table_5_0(self):
        self.assertEqual(create_table(5, 0), [])

    def test_create_table_2_3(self):
        self.assertEqual(create_table(2, 3), [[1, 1, 1], [1, 2, 3]])
    
    def test_create_table_m_equals_1(self):
        expected_result = [[1, 1, 1]]
        result = create_table(1, 3)
        self.assertEqual(result, expected_result)


class TestFlatten(unittest.TestCase):
    def test_flatten_1(self):
        self.assertEqual(flatten([1, [2]]), [1, 2])

    def test_flatten_2(self):
        self.assertEqual(flatten([1, 2, [3, [4, 5], 6], 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_flatten_3(self):
        self.assertEqual(flatten(['wow', [2, [[]]], [True]]), ['wow', 2, True])

    def test_flatten_4(self):
        self.assertEqual(flatten([]), [])

    def test_flatten_5(self):
        self.assertEqual(flatten([[]]), [])

    def test_flatten_6(self):
        self.assertEqual(flatten(3), 3)

# Об'єднання схожих тестів в один тестовий набір
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCreateTable('test_create_table_4_6'))
    suite.addTest(TestCreateTable('test_create_table_1_1'))
    suite.addTest(TestCreateTable('test_create_table_0_5'))
    suite.addTest(TestCreateTable('test_create_table_5_0'))
    suite.addTest(TestCreateTable('test_create_table_2_3'))
    suite.addTest(TestFlatten('test_flatten_1'))
    suite.addTest(TestFlatten('test_flatten_2'))
    suite.addTest(TestFlatten('test_flatten_3'))
    suite.addTest(TestFlatten('test_flatten_4'))
    suite.addTest(TestFlatten('test_flatten_5'))
    suite.addTest(TestFlatten('test_flatten_6'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())