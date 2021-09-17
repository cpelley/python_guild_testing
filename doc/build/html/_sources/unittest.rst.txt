Unittest
========

- Unit testing is the idea of testing the 'smallest' separable (reasonable) source 'unit'.
- These should run very fast.
- Python `unittest <https://docs.python.org/3/library/unittest.html>`_ is the primary unit test framework, allowing us to test in a standard and easy way.
  - The framework is not exclusive to the category known as unit testing.
  - Many other testing frameworks exist, however these most often are built upon this unittest package.  We will mention some of the most notable later.
- Generally, each code pathway represents a unit to be tested and is done at the function level.  Tools like McCabe Cyclomatic Complexity metric calculate test coverage or 'code complexity' relates to this concept by identifying code pathways.

In this dummy package, we provide examples unit tests:
:source:`test_get_array_slice.py <tests/test_get_array_slice.py>` for unittesting the
:func:`nslice.get_array_slice` function and :source:`test_get_array_slice.py <tests/test_group_indices.py>`
for unittesting the :func:`nslice.group_indices` function of our package.

A good approach is to structure tests in such a way that it reflects the hierarchy and layout of the code.
This aids transparency, discoverability and maintenance. To illustrate, if we were to test a class method: ``<package>.<module>.<Class>.<method>``,
we would then have an associated unittest at ``<package>/tests/<module>/<class>/test_<method>.py``.

Note that the prefix of 'test_' is by default a means to aid discoverability and identification of tests and that it is good practice to test all public functions and classes.

Other testing frameworks
------------------------
`nose <https://pypi.org/project/nose/>`_ is a useful testing framework built upon the python unittest framework, providing extra capability like running tests in parallel, running and discovery of doctests, useful additional syntax in writing tests etc.
However, nose has been deprecated and should likely no longer be the chosen framework for new packages.

`pytest <https://pytest.org/>`_ is good alternative to nose and is increasingly one of the most popular testing
frameworks, with out of the box benefits including improved readability of test output.
It also provides potentially useful extra capability when writing tests and well as a plug-in based approach to further capabilities still (like parallel running of tests).

Advanced testing
----------------
Arguably a more advanced tool in aid of unit testing is with use of
`unittest.mock <https://docs.python.org/3/library/unittest.mock.html>`_.  Useful for replacing parts of
your system under test with mock objects and allowing us to make assertions about how they have been used.
In the strict sense, this enables us to test our 'unit' in true isolation of other code.  Care should be given when
using such tools, since overuse can lead down a rabbit hole making the code under test difficult to change as tests
become increasingly complex and difficult to understand.

Potentially we might also have an integration test to ensure this class serves its purpose as a component of a larger chain at ``<package>/tests/<module>/test_integration.py``

integration tests
=================

I think it useful to draw a distinction here between unit tests and integration tests.  While unit tests test our
smallest source 'unit', integration tests test these our components (functions/classes etc.) actually successfully
interact with one another (as we expect).

For example, let's say that the output of ``function1`` gets fed into the input of ``function2``, then it would be
desirable to ensure that these two separate components can indeed interact with one another as we expect.

An example in this package is :source:`test_integration.py <tests/test_integration.py>`, which calls the top-level
public :func:`nslice.sliceme` function.  This ensures successful interaction between the underlying functions that it
calls (:func:`nslice.get_array_slice` and :func:`nslice.group_indices`) and that it returns a result we expect.

Integration tests should still be small as reasonable and run very quickly.

acceptance tests
================

- Acceptance testing is about ensuring the end-to-end running of your code for one or more usecase.
- You don't care so much about the details of how or with what it got to the end result, only that it got there.
- Array checks, graphical testing, or file checking may be relevant in this context.
- These may not run fast, though perhaps there are different levels of acceptance testing (full slow real ones and perhaps more frequently run fictitious end-to-end ones?).
- No guarantee that given an even slightly different usecase that it won't break your program or worse (return incorrect results) - that's what unit tests and integration tests are for.

Code style checks
=================

Familiar code is easy to read and understand and maintain while heavily personalised code preferences are not.

These standards have basis from experienced software engineers of what has proven to be easier and neater to both
understand and maintain.

Typically, for Python these normally have basis in PEP guidelines for good
style. Such as those for line length, naming conventions (camel case class
names, ...).

See "zen on python" (`pep 20 <https://www.python.org/dev/peps/pep-0020/>`_) as it is worth a read!

Useful tools
------------
Typical tools of interest for code style/off-line testing include:

- `pycodestyle <https://pycodestyle.pycqa.org/en/latest/intro.html>`_ (`pep8 <https://www.python.org/dev/peps/pep-0008/>`_ checks).
- `pyflakes <https://github.com/PyCQA/pyflakes>`_ (off-line code error checking).
- `flake8 <https://flake8.pycqa.org/en/latest/>`_ (framework with plug-in support for numerous checks).
- `pylint <https://pylint.org/>`_, for performing a code analysis and scoring it.
- `black <https://black.readthedocs.io/en/stable/>`_ (code auto formatter).

Of particular note here is "black", since it allows the developer the freedom to avoid issues around
`pep8 <https://www.python.org/dev/peps/pep-0008/>`_ compliance and minimise issues relating to personal preference
(when it comes to style at least) at code review.  Black takes change of these issues and decides on your behalf.
