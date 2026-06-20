# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_intenum_from_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(IntStooges.from_bytes(b'\x00\x03', 'big'), IntStooges.MOE)
    with self.assertRaises(ValueError):
        IntStooges.from_bytes(b'\x00\x05', 'big')
