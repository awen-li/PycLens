# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class OrdinaryEnum(Enum):
        a = 1
    self.assertEqual(ALWAYS_EQ, OrdinaryEnum.a)
    self.assertEqual(OrdinaryEnum.a, ALWAYS_EQ)
