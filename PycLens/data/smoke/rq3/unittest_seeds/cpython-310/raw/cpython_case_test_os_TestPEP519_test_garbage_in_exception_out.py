# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestPEP519_test_garbage_in_exception_out

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    vapor = type('blah', (), {})
    for o in (int, type, os, vapor()):
        self.assertRaises(TypeError, self.fspath, o)
