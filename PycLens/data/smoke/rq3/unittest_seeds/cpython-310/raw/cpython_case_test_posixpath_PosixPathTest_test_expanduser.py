# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_expanduser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(posixpath.expanduser('foo'), 'foo')
    self.assertEqual(posixpath.expanduser(b'foo'), b'foo')
