# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b32decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertEqual
    tests = {b'': b'', b'AA======': b'\x00', b'ME======': b'a', b'MFRA====': b'ab', b'MFRGG===': b'abc', b'MFRGGZA=': b'abcd', b'MFRGGZDF': b'abcde'}
    for (data, res) in tests.items():
        eq(base64.b32decode(data), res)
        eq(base64.b32decode(data.decode('ascii')), res)
    self.check_other_types(base64.b32decode, b'MFRGG===', b'abc')
    self.check_decode_type_errors(base64.b32decode)
