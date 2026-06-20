# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_floatenum_fromhex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = float.hex(FloatStooges.MOE.value)
    self.assertIs(FloatStooges.fromhex(h), FloatStooges.MOE)
    h = float.hex(FloatStooges.MOE.value + 0.01)
    with self.assertRaises(ValueError):
        FloatStooges.fromhex(h)
