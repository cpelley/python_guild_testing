import unittest
from unittest import mock

from nslice import get_array_slice as sliceme


class TestAll(unittest.TestCase):
    def test_call(self):
        group_ind_patch = mock.patch('nslice.group_indices')
        z = mock.MagicMock('array')

        with group_ind_patch as group_ind_patched:
            # Let's have our patch return the thing that is passed to it.
            # Make it easy to check ordering of how y and x are used.
            group_ind_patched.side_effect = lambda x: [x]
            res = sliceme(z, [mock.sentinel.y, mock.sentinel.x])

        # if the API of group_ind_patched was any more complicated, we could
        # check what we pass it.  We leave that for the integration test.
        # ...

        # Check how the getitem was called
        z.__getitem__.assert_called_once_with((mock.sentinel.y, mock.sentinel.x))
        # Check what is actually returned is the getitem return
        self.assertEqual(res, z[mock.sentinel.x, mock.sentinel.y])


class TestExceptions(unittest.TestCase):
    def test_not_one_2d_chunk(self):
        group_ind_patch = mock.patch('nslice.group_indices')
        z = mock.MagicMock('array')

        with group_ind_patch as group_ind_patched:
            # Let's have our patch return the thing that is passed to it.
            # Make it easy to check ordering of how y and x are used.
            group_ind_patched.side_effect = lambda x: [x, x]

            msg = 'Unable to fetch one consecutive chunk for dimension 0'
            with self.assertRaisesRegex(ValueError, msg):
                sliceme(z, [mock.sentinel.y, mock.sentinel.x])


if __name__ == '__main__':
    unittest.main()
