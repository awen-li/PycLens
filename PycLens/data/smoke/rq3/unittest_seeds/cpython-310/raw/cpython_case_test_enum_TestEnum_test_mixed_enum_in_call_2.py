# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_mixed_enum_in_call_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Monochrome(Enum):
        black = 0
        white = 1

    class Gender(IntEnum):
        male = 0
        female = 1
    self.assertIs(Monochrome(Gender.male), Monochrome.black)
