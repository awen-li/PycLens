# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_ord

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'\x00A\x7f\x80\xff')
    self.assertEqual([ord(b[i:i + 1]) for i in range(len(b))], [0, 65, 127, 128, 255])
