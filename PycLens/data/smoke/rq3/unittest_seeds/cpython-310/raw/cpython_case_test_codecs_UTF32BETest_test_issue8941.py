# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF32BETest_test_issue8941

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoded = b'\x00\x01\x00\x00' * 1024
    self.assertEqual('𐀀' * 1024, codecs.utf_32_be_decode(encoded)[0])
