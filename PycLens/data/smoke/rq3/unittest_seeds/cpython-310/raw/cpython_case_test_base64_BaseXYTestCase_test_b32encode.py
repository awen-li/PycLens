# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b32encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    eq(base64.b32encode(b''), b'')
    eq(base64.b32encode(b'\x00'), b'AA======')
    eq(base64.b32encode(b'a'), b'ME======')
    eq(base64.b32encode(b'ab'), b'MFRA====')
    eq(base64.b32encode(b'abc'), b'MFRGG===')
    eq(base64.b32encode(b'abcd'), b'MFRGGZA=')
    eq(base64.b32encode(b'abcde'), b'MFRGGZDF')
    self.check_other_types(base64.b32encode, b'abcd', b'MFRGGZA=')
    self.check_encode_type_errors(base64.b32encode)
