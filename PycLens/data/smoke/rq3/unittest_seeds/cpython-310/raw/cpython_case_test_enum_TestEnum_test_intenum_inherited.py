# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_intenum_inherited

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class IntEnum(int, Enum):
        pass

    class phy(IntEnum):
        pi = 3
        tau = 2 * pi
    self.assertTrue(phy.pi < phy.tau)
