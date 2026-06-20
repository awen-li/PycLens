# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: LegacyBase64TestCase_test_encodebytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(base64.encodebytes(b'www.python.org'), b'd3d3LnB5dGhvbi5vcmc=\n')
    eq(base64.encodebytes(b'a'), b'YQ==\n')
    eq(base64.encodebytes(b'ab'), b'YWI=\n')
    eq(base64.encodebytes(b'abc'), b'YWJj\n')
    eq(base64.encodebytes(b''), b'')
    eq(base64.encodebytes(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}'), b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0\nNTY3ODkhQCMwXiYqKCk7Ojw+LC4gW117fQ==\n')
    eq(base64.encodebytes(bytearray(b'abc')), b'YWJj\n')
    eq(base64.encodebytes(memoryview(b'abc')), b'YWJj\n')
    eq(base64.encodebytes(array('B', b'abc')), b'YWJj\n')
    self.check_type_errors(base64.encodebytes)
