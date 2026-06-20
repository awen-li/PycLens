# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_DirsOnSysPath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with import_helper.DirsOnSysPath('foo', 'bar'):
        self.assertIn('foo', sys.path)
        self.assertIn('bar', sys.path)
    self.assertNotIn('foo', sys.path)
    self.assertNotIn('bar', sys.path)
