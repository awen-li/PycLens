# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_docstring

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        f'Not a docstring'
    self.assertIsNone(f.__doc__)

    def g():
        f'Not a docstring'
    self.assertIsNone(g.__doc__)
