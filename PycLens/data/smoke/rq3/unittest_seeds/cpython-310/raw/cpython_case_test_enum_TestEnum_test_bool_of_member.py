# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_bool_of_member

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Count(Enum):
        zero = 0
        one = 1
        two = 2
    for member in Count:
        self.assertTrue(bool(member))
