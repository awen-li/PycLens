# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_from_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(bool.from_bytes(b'\x00' * 8, 'big'), False)
    self.assertIs(bool.from_bytes(b'abcd', 'little'), True)
