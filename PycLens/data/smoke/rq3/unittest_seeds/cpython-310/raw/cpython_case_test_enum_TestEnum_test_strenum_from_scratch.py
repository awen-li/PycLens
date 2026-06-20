# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_strenum_from_scratch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class phy(str, Enum):
        pi = 'Pi'
        tau = 'Tau'
    self.assertTrue(phy.pi < phy.tau)
