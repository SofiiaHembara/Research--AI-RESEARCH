from initial_code import find_max_1, find_max_2, compute_limit, compute_derivative, get_root, get_tangent
import unittest

class TestCalculationFunctions(unittest.TestCase):

    def test_find_max_1_empty_list(self):
        """Test find_max_1 with an empty list."""
        f = lambda x: x**2
        points = []
        with self.assertRaises(ValueError):
            find_max_1(f, points)

    def test_find_max_1_single_element(self):
        """Test find_max_1 with a list containing a single element."""
        f = lambda x: x**2
        points = [1]
        self.assertEqual(find_max_1(f, points), 1)

    def test_find_max_1_negative_values(self):
        """Test find_max_1 with a list containing only negative values."""
        f = lambda x: x**2
        points = [-1, -2, -3]
        self.assertEqual(find_max_1(f, points), 1)

    def test_find_max_1_mixed_values(self):
        """Test find_max_1 with a list containing positive and negative values."""
        f = lambda x: x**2
        points = [1, 4, 2, -3]
        self.assertEqual(find_max_1(f, points), 16)

    def test_find_max_2_empty_list(self):
        """Test find_max_2 with an empty list."""
        f = lambda x: x**2
        points = []
        self.assertEqual(find_max_2(f, points), [])

    def test_find_max_2_multiple_maxima(self):
        """Test find_max_2 with a list where multiple points have the maximum value."""
        f = lambda x: x**2
        points = [1, 4, 4, 2]
        self.assertEqual(find_max_2(f, points), [4, 4])

    def test_find_max_2_single_maximum(self):
        """Test find_max_2 with a list where a single point has the maximum value."""
        f = lambda x: x**2
        points = [1, 4, 2, 3]
        self.assertEqual(find_max_2(f, points), [4])

    # Add tests for compute_limit, compute_derivative, get_tangent, and get_root

if __name__ == "__main__":
    unittest.main()