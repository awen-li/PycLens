# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_base64.py
# case: BaseXYTestCase_test_b32hexdecode_other_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_other_types(base64.b32hexdecode, b'C5H66===', b'abc')
    self.check_decode_type_errors(base64.b32hexdecode)
