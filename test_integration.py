import numpy as np

import unittest
from example_doctest import sliceme_one_consequtive_chunk as sliceme


class TestAll(unittest.TestCase):
    def test_value(self):
        z = np.arange(24).reshape(6, 4)
        x_indx = [0, 1]
        y_indx = [4, 5]
        res = sliceme(z, y_indx, x_indx)
        tar = z[y_indx][..., x_indx]
        self.assertTrue(np.array_equal(res, tar))


if __name__ == '__main__':
    unittest.main()
