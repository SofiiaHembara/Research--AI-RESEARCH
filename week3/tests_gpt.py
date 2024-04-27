from initial_code import find_max_1, find_max_2, compute_limit, compute_derivative, get_root, get_tangent
import unittest

class TestFunctions(unittest.TestCase):

    def test_find_max_1(self):
        self.assertEqual(find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1]), 12)

    def test_find_max_2(self):
        self.assertEqual(find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1]), [3])

    def test_compute_limit(self):
        self.assertEqual(compute_limit(lambda n: (n ** 2 + n) / n ** 2), 1.0)

    def test_compute_derivative(self):
        self.assertAlmostEqual(compute_derivative(lambda x: x ** 2 + x, 2), 5.0)

    def test_get_tangent(self):
        self.assertEqual(get_tangent(lambda x: x ** 2 + x, 2), '5.0 * x - 4.0')

    def test_get_root(self):
        self.assertAlmostEqual(get_root(lambda x: x, -1, 1), 0.0)


if __name__ == '__main__':
    unittest.main()
