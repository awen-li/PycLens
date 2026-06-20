# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b16encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(base64.b16encode(b'\x01\x02\xab\xcd\xef'), b'0102ABCDEF')
    eq(base64.b16encode(b'\x00'), b'00')
    self.check_other_types(base64.b16encode, b'\x01\x02\xab\xcd\xef', b'0102ABCDEF')
    self.check_encode_type_errors(base64.b16encode)
