# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b32decode_casefold

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    tests = {b'': b'', b'ME======': b'a', b'MFRA====': b'ab', b'MFRGG===': b'abc', b'MFRGGZA=': b'abcd', b'MFRGGZDF': b'abcde', b'me======': b'a', b'mfra====': b'ab', b'mfrgg===': b'abc', b'mfrggza=': b'abcd', b'mfrggzdf': b'abcde'}
    for (data, res) in tests.items():
        eq(base64.b32decode(data, True), res)
        eq(base64.b32decode(data.decode('ascii'), True), res)
    self.assertRaises(binascii.Error, base64.b32decode, b'me======')
    self.assertRaises(binascii.Error, base64.b32decode, 'me======')
    eq(base64.b32decode(b'MLO23456'), b'b\xdd\xad\xf3\xbe')
    eq(base64.b32decode('MLO23456'), b'b\xdd\xad\xf3\xbe')
    map_tests = {(b'M1023456', b'L'): b'b\xdd\xad\xf3\xbe', (b'M1023456', b'I'): b'b\x1d\xad\xf3\xbe'}
    for ((data, map01), res) in map_tests.items():
        data_str = data.decode('ascii')
        map01_str = map01.decode('ascii')
        eq(base64.b32decode(data, map01=map01), res)
        eq(base64.b32decode(data_str, map01=map01), res)
        eq(base64.b32decode(data, map01=map01_str), res)
        eq(base64.b32decode(data_str, map01=map01_str), res)
        self.assertRaises(binascii.Error, base64.b32decode, data)
        self.assertRaises(binascii.Error, base64.b32decode, data_str)
