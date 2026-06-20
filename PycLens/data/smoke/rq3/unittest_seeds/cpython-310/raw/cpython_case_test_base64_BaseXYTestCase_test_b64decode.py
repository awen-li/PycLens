# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b64decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    tests = {b'd3d3LnB5dGhvbi5vcmc=': b'www.python.org', b'AA==': b'\x00', b'YQ==': b'a', b'YWI=': b'ab', b'YWJj': b'abc', b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0\nNTY3ODkhQCMwXiYqKCk7Ojw+LC4gW117fQ==': b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}', b'': b''}
    for (data, res) in tests.items():
        eq(base64.b64decode(data), res)
        eq(base64.b64decode(data.decode('ascii')), res)
    self.check_other_types(base64.b64decode, b'YWJj', b'abc')
    self.check_decode_type_errors(base64.b64decode)
    tests_altchars = {(b'01a*b$cd', b'*$'): b'\xd3V\xbeo\xf7\x1d'}
    for ((data, altchars), res) in tests_altchars.items():
        data_str = data.decode('ascii')
        altchars_str = altchars.decode('ascii')
        eq(base64.b64decode(data, altchars=altchars), res)
        eq(base64.b64decode(data_str, altchars=altchars), res)
        eq(base64.b64decode(data, altchars=altchars_str), res)
        eq(base64.b64decode(data_str, altchars=altchars_str), res)
    for (data, res) in tests.items():
        eq(base64.standard_b64decode(data), res)
        eq(base64.standard_b64decode(data.decode('ascii')), res)
    self.check_other_types(base64.standard_b64decode, b'YWJj', b'abc')
    self.check_decode_type_errors(base64.standard_b64decode)
    tests_urlsafe = {b'01a-b_cd': b'\xd3V\xbeo\xf7\x1d', b'': b''}
    for (data, res) in tests_urlsafe.items():
        eq(base64.urlsafe_b64decode(data), res)
        eq(base64.urlsafe_b64decode(data.decode('ascii')), res)
    self.check_other_types(base64.urlsafe_b64decode, b'01a-b_cd', b'\xd3V\xbeo\xf7\x1d')
    self.check_decode_type_errors(base64.urlsafe_b64decode)
