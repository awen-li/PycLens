# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestPEP519_test_bad_pathlike

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.fspath, FakePath(42))
    c = type('foo', (), {})
    c.__fspath__ = 1
    self.assertRaises(TypeError, self.fspath, c())
    self.assertRaises(ZeroDivisionError, self.fspath, FakePath(ZeroDivisionError()))
