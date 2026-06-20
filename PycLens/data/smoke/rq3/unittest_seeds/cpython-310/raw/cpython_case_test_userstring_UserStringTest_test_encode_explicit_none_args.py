# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_userstring.py
# case: UserStringTest_test_encode_explicit_none_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkequal(b'hello', 'hello', 'encode', None, None)
    self.checkequal(b'\xf0\xa3\x91\x96', '𣑖', 'encode', None, None)
    self.checkraises(UnicodeError, '\ud800', 'encode', None, None)
