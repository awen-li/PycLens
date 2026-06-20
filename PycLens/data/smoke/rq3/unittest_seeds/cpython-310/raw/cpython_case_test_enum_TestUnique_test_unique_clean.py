# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestUnique_test_unique_clean

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @unique
    class Clean(Enum):
        one = 1
        two = 'dos'
        tres = 4.0

    @unique
    class Cleaner(IntEnum):
        single = 1
        double = 2
        triple = 3
