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


def sliceme_one_2d_chunk(z, y_indx, x_indx):
    """
    Fetch a single 2D chunk from the provided array.

    This fictitious function essentially turns the array-like indices into
    slice objects in order to return a single 2D slice of `z`.

    Parameters
    ----------
    z : :class:`numpy.ndarray`
        The array we would like to slice.
    y_indx : 1D array-like
        The 'y' indices we want to slice from the provided array (z).
    x_indx : 1D array-like
        The 'x' indices we want to slice from the provided array (z).

    Return
    ------
    : :class:`numpy.ndarray`
        The 'z' array sliced by the provided indices such as to return a single
        chunk.

    Raises
    ------
    ValueError
        Where a single 2D slice cannot be returned using the provided indices.

    """
    x_slice = group_indices(x_indx)
    y_slice = group_indices(y_indx)

    if len(x_slice) != 1 or len(y_slice) != 1:
        msg = 'Unable to fetch one consecutive chunk.  y_slice:{} x_slice:{}'
        raise ValueError(msg.format(y_slice, x_slice))
    return z[y_slice[0], x_slice[0]]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
