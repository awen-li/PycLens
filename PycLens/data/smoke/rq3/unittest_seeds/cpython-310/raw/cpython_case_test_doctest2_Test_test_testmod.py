# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_doctest2.py
# case: Test_test_testmod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import doctest, sys
    EXPECTED = 19
    (f, t) = doctest.testmod(sys.modules[__name__])
    if f:
        self.fail('%d of %d doctests failed' % (f, t))
    if t != EXPECTED:
        self.fail('expected %d tests to run, not %d' % (EXPECTED, t))
