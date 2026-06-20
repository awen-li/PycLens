# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b16decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(base64.b16decode(b'0102ABCDEF'), b'\x01\x02\xab\xcd\xef')
    eq(base64.b16decode('0102ABCDEF'), b'\x01\x02\xab\xcd\xef')
    eq(base64.b16decode(b'00'), b'\x00')
    eq(base64.b16decode('00'), b'\x00')
    self.assertRaises(binascii.Error, base64.b16decode, b'0102abcdef')
    self.assertRaises(binascii.Error, base64.b16decode, '0102abcdef')
    eq(base64.b16decode(b'0102abcdef', True), b'\x01\x02\xab\xcd\xef')
    eq(base64.b16decode('0102abcdef', True), b'\x01\x02\xab\xcd\xef')
    self.check_other_types(base64.b16decode, b'0102ABCDEF', b'\x01\x02\xab\xcd\xef')
    self.check_decode_type_errors(base64.b16decode)
    eq(base64.b16decode(bytearray(b'0102abcdef'), True), b'\x01\x02\xab\xcd\xef')
    eq(base64.b16decode(memoryview(b'0102abcdef'), True), b'\x01\x02\xab\xcd\xef')
    eq(base64.b16decode(array('B', b'0102abcdef'), True), b'\x01\x02\xab\xcd\xef')
    self.assertRaises(binascii.Error, base64.b16decode, '0102AG')
    self.assertRaises(binascii.Error, base64.b16decode, '010')
