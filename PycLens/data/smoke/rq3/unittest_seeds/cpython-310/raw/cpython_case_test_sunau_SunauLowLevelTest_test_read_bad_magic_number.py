# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sunau.py
# case: SunauLowLevelTest_test_read_bad_magic_number

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = b'SPA'
    with self.assertRaises(EOFError):
        sunau.open(io.BytesIO(b))
    b = b'SPAM'
    with self.assertRaisesRegex(sunau.Error, 'bad magic number'):
        sunau.open(io.BytesIO(b))
