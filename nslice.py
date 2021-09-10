import numpy as np


__version__ = "0.1"


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

    Examples
    --------

    >>> from nslice import group_indices
    >>> import numpy as np
    >>> indices = np.array([0, 1, 2, 4, 5, 6, 8, 9])
    >>> group_indices(indices)
    [slice(0, 3, None), slice(4, 7, None), slice(8, 10, None)]

    """
    array = np.asarray(array)
    if array.ndim != 1:
        msg = 'Excepting a 1D array, got a {}D one.'
        raise ValueError(msg.format(array.ndim))

    diff = np.diff(array)
    diff = np.hstack([np.where(diff != 1)[0], diff.size])
    ref = 0
    slices = []
    for dd in range(len(diff)):
        slices.append(slice(array[ref], array[diff[dd]] + 1))
        ref = diff[dd] + 1
    return slices


def get_array_slice(z, indices):
    """
    Fetch a single chunk from the provided array.

    This fictitious function essentially turns the array-like indices into
    slice objects in order to return a single N-dimensional slice of `z`.
    The dimensionality of this chunk will match the dimensionality of the
    provided array.

    Parameters
    ----------
    z : :class:`numpy.ndarray`
        The array we would like to slice.
    indices : iterable of 1D array-like objects
        Indices we want to slice from the provided array (z) for each dimension.

    Return
    ------
    : :class:`numpy.ndarray`
        The 'z' array sliced by the provided indices such as to return a single
        chunk.

    Raises
    ------
    ValueError
        Where a single chunk cannot be returned using the provided indices.

    """
    groups = []
    for ind, index_array in enumerate(indices):
        groups.append(group_indices(index_array))
        if len(groups[-1]) != 1:
            msg = f"Unable to fetch one consecutive chunk for dimension {ind}"
            raise ValueError(msg)
        groups[-1] = groups[-1][0]
    return z[tuple(groups)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
