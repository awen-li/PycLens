# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: CommonTest_test_realpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIn('foo', self.pathmodule.realpath('foo'))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        self.assertIn(b'foo', self.pathmodule.realpath(b'foo'))
