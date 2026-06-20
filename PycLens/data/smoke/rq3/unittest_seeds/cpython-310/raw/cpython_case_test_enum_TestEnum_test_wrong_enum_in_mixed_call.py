# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_wrong_enum_in_mixed_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Monochrome(IntEnum):
        black = 0
        white = 1

    class Gender(Enum):
        male = 0
        female = 1
    self.assertRaises(ValueError, Monochrome, Gender.male)
