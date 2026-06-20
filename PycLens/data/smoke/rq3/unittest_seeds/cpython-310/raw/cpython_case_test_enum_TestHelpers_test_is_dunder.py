# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestHelpers_test_is_dunder

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('__a__', '__aa__'):
        self.assertTrue(enum._is_dunder(s))
    for s in ('a', 'a_', '_a', '__a', 'a__', '_a_', '_a__', '__a_', '_', '__', '___', '____', '_____'):
        self.assertFalse(enum._is_dunder(s))
