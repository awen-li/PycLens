# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b64encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(base64.b64encode(b'www.python.org'), b'd3d3LnB5dGhvbi5vcmc=')
    eq(base64.b64encode(b'\x00'), b'AA==')
    eq(base64.b64encode(b'a'), b'YQ==')
    eq(base64.b64encode(b'ab'), b'YWI=')
    eq(base64.b64encode(b'abc'), b'YWJj')
    eq(base64.b64encode(b''), b'')
    eq(base64.b64encode(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}'), b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0NTY3ODkhQCMwXiYqKCk7Ojw+LC4gW117fQ==')
    eq(base64.b64encode(b'\xd3V\xbeo\xf7\x1d', altchars=b'*$'), b'01a*b$cd')
    eq(base64.b64encode(b'\xd3V\xbeo\xf7\x1d', altchars=bytearray(b'*$')), b'01a*b$cd')
    eq(base64.b64encode(b'\xd3V\xbeo\xf7\x1d', altchars=memoryview(b'*$')), b'01a*b$cd')
    eq(base64.b64encode(b'\xd3V\xbeo\xf7\x1d', altchars=array('B', b'*$')), b'01a*b$cd')
    self.check_other_types(base64.b64encode, b'abcd', b'YWJjZA==')
    self.check_encode_type_errors(base64.b64encode)
    self.assertRaises(TypeError, base64.b64encode, b'', altchars='*$')
    eq(base64.standard_b64encode(b'www.python.org'), b'd3d3LnB5dGhvbi5vcmc=')
    eq(base64.standard_b64encode(b'a'), b'YQ==')
    eq(base64.standard_b64encode(b'ab'), b'YWI=')
    eq(base64.standard_b64encode(b'abc'), b'YWJj')
    eq(base64.standard_b64encode(b''), b'')
    eq(base64.standard_b64encode(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}'), b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0NTY3ODkhQCMwXiYqKCk7Ojw+LC4gW117fQ==')
    self.check_other_types(base64.standard_b64encode, b'abcd', b'YWJjZA==')
    self.check_encode_type_errors(base64.standard_b64encode)
    eq(base64.urlsafe_b64encode(b'\xd3V\xbeo\xf7\x1d'), b'01a-b_cd')
    self.check_other_types(base64.urlsafe_b64encode, b'\xd3V\xbeo\xf7\x1d', b'01a-b_cd')
    self.check_encode_type_errors(base64.urlsafe_b64encode)
