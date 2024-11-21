"""Template for Lesson 11 In-Class Exercise on testing"""

from quadratic import quadratic_roots
import unittest

class TestQuadratic(unittest.TestCase):

    def test_no_roots(self):
        """check that an empty list is returned when no solution"""
        roots = quadratic_roots(1., 0., 1.)
        self.assertTrue(len(roots)==0)

    def test_one_root(self):
        """test when quadratic has only one solution"""
        # Add your test here
        a, b, c = 1, -2, 1
        expected_root = [1.0]
        roots = quadratic_roots(a,b,c)
        self.assertEqual(len(roots), 1)
        self.assertAlmostEqual(roots[0], expected_root[0])
    def test_two_roots(self):
        """test when quadratic has two solutions"""
        # Add your test here
        a, b, c = 1, -3, 2
        expected_roots = [1.0, 2.0]
        actual_roots = quadratic_roots(a, b, c)
        
        self.assertAlmostEqual(actual_roots[0], expected_roots[0])
        self.assertAlmostEqual(actual_roots[1], expected_roots[1])
        self.assertEqual(len(actual_roots), 2)
        self.assertEqual(actual_roots[0], min(actual_roots))  # Ensuring order
        self.assertEqual(actual_roots[1], max(actual_roots))

if __name__ == '__main__':
    unittest.main()
