# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_hqx

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rle = binascii.rlecode_hqx(self.data)
    a = binascii.b2a_hqx(self.type2test(rle))
    (b, _) = binascii.a2b_hqx(self.type2test(a))
    res = binascii.rledecode_hqx(b)
    self.assertEqual(res, self.rawdata)
