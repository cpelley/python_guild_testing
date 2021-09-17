Doctests
========

Doctests are used to test interactive python examples and are a way of demonstrating how your code should be used.
Sometimes an example is worth 10x more than words.
They ensure that your documented example does not become out of date with code changes but should generally not be used **instead** of other forms of testing (use in addition to them).

Doctests can take the form of those which are included as part of our sphinx rst files, or the more traditional doctests which are part of our usual docstrings.

This later case we will look at first:

.. autofunction:: nslice::group_indices

Under the hood these doctests are run via the `doctest <https://docs.python.org/3/library/doctest.html>`_ python package.  At the bottom of the module where this function lives, we include the following snippet to enable us to run doctests present in this module when we run this module: ::

    if __name__ == "__main__":                                                     
        import doctest                                                             
        doctest.testmod()

However, it would be impractical and in all likelihood undesirable to do this for all our modules/packages.  For convenience we can simply use `pytest <https://pytest.org/>`_ to perform both unittest and doctest discovery for us: ::

    pytest --doctest-modules

Alternatively, we can run doctests included in our docstrings using the `sphinx doctest <http://www.sphinx-doc.org/en/stable/ext/doctest.html>`_ extension.
This can then be done by calling `make doctest` for our sphinx package documentation.

However it should be noted that there is a difference in behaviour of sphinx doctests run behaviour and those run more directly by doctest (using doctest, pytest etc.).
Take a look:

sphinx incompatible, doctest compatible: ::

    >>> indices = np.array([0, 1, 2, 4, 5, 6, 8, 9])
    >>> group_indices(indices)
    [slice(0, 3, None), slice(4, 7, None), slice(8, 10, None)]

sphinx compatible, doctest compatible: ::

    >>> from nslice import group_indices
    >>> import numpy as np
    >>> indices = np.array([0, 1, 2, 4, 5, 6, 8, 9])
    >>> group_indices(indices)
    [slice(0, 3, None), slice(4, 7, None), slice(8, 10, None)]

Sphinx reads the python module and translates it to reST code where the module namespace is then not accessible to the doctest.
This is why we had to add the two above `include` lines.
