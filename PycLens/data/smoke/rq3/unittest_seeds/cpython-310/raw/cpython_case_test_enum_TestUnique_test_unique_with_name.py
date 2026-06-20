# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestUnique_test_unique_with_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @unique
    class Silly(Enum):
        one = 1
        two = 'dos'
        name = 3

    @unique
    class Sillier(IntEnum):
        single = 1
        name = 2
        triple = 3
        value = 4
