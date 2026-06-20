# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_center

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'abc')
    for fill_type in (bytes, bytearray):
        self.assertEqual(b.center(7, fill_type(b'-')), self.type2test(b'--abc--'))
