import numpy as np

import unittest
from example_doctest import group_indices


class Test1D(unittest.TestCase):
    def setUp(self):
        self.indices = [0, 1, 2, 4, 5, 6, 8, 9]

    def assert_group_indices(self, indices):
        res = group_indices(indices)
        tar = [slice(0, 3, None), slice(4, 7, None), slice(8, 10, None)]
        self.assertEqual(res, tar)

    def test_array(self):
        self.assert_group_indices(np.array(self.indices))

    def test_lists(self):
        self.assert_group_indices(self.indices)


class TestExceptions(unittest.TestCase):
    def test_nd(self):
        indices = np.array([0, 1, 2, 4, 5, 6, 8, 9]).reshape((2, 4))
        msg = 'Excepting a 1D array, got a 2D one.'
        with self.assertRaisesRegexp(ValueError, msg):
            res = group_indices(indices)


if __name__ == '__main__':
    unittest.main()
