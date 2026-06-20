# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: LegacyBase64TestCase_test_decodebytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(base64.decodebytes(b'd3d3LnB5dGhvbi5vcmc=\n'), b'www.python.org')
    eq(base64.decodebytes(b'YQ==\n'), b'a')
    eq(base64.decodebytes(b'YWI=\n'), b'ab')
    eq(base64.decodebytes(b'YWJj\n'), b'abc')
    eq(base64.decodebytes(b'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM0\nNTY3ODkhQCMwXiYqKCk7Ojw+LC4gW117fQ==\n'), b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#0^&*();:<>,. []{}')
    eq(base64.decodebytes(b''), b'')
    eq(base64.decodebytes(bytearray(b'YWJj\n')), b'abc')
    eq(base64.decodebytes(memoryview(b'YWJj\n')), b'abc')
    eq(base64.decodebytes(array('B', b'YWJj\n')), b'abc')
    self.check_type_errors(base64.decodebytes)
