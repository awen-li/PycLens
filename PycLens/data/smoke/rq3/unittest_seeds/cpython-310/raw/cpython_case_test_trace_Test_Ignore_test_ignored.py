# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: Test_Ignore_test_ignored

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    jn = os.path.join
    ignore = trace._Ignore(['x', 'y.z'], [jn('foo', 'bar')])
    self.assertTrue(ignore.names('x.py', 'x'))
    self.assertFalse(ignore.names('xy.py', 'xy'))
    self.assertFalse(ignore.names('y.py', 'y'))
    self.assertTrue(ignore.names(jn('foo', 'bar', 'baz.py'), 'baz'))
    self.assertFalse(ignore.names(jn('bar', 'z.py'), 'z'))
    self.assertTrue(ignore.names(jn('bar', 'baz.py'), 'baz'))
