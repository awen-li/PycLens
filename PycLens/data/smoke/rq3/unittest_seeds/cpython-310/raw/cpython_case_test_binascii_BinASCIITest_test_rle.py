# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_rle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'a' * 100 + b'b' + b'c' * 300
    encoded = binascii.rlecode_hqx(data)
    self.assertEqual(encoded, b'a\x90dbc\x90\xffc\x90-')
    decoded = binascii.rledecode_hqx(encoded)
    self.assertEqual(decoded, data)
