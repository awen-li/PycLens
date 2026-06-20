# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_tuples

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertGdbRepr(tuple(), '()')
    self.assertGdbRepr((1,), '(1,)')
    self.assertGdbRepr(('foo', 'bar', 'baz'))
