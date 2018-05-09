import numpy as np


def group_indices(array):
    """
    Group an array representing indices into an iterable of slice objects.

    Parameters
    ----------
    array : :class:`numpy.ndarray`
        Numpy array representing indices.

    Returns
    -------
    : iterable of slice objects

    >>> indices = np.array([0, 1, 2, 4, 5, 6, 8, 9])
    >>> group_indices(indices)
    [slice(0, 3, None), slice(4, 7, None), slice(8, 10, None)]

    """
    diff = np.diff(array)
    diff = np.hstack([np.where(diff != 1)[0], diff.size])
    ref = 0
    slices = []
    for dd in range(len(diff)):
        slices.append(slice(array[ref], array[diff[dd]] + 1))
        ref = diff[dd] + 1
    return slices


if __name__ == "__main__":
    import doctest
    doctest.testmod()
