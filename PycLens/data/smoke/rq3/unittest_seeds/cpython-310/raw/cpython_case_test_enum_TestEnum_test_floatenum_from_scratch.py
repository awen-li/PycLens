# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_floatenum_from_scratch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class phy(float, Enum):
        pi = 3.1415926
        tau = 2 * pi
    self.assertTrue(phy.pi < phy.tau)
