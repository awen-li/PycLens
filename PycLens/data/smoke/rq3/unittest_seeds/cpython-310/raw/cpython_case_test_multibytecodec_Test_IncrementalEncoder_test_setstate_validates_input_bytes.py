# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_IncrementalEncoder_test_setstate_validates_input_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoder = codecs.getincrementalencoder('euc_jp')()
    invalid_utf8 = int.from_bytes(b'\x01\xff\x00\x00\x00\x00\x00\x00\x00\x00', 'little')
    self.assertRaises(UnicodeDecodeError, encoder.setstate, invalid_utf8)
