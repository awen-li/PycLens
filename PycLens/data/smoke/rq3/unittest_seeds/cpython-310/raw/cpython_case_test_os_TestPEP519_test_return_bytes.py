# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestPEP519_test_return_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for b in (b'hello', b'goodbye', b'some/path/and/file'):
        self.assertEqual(b, self.fspath(b))
