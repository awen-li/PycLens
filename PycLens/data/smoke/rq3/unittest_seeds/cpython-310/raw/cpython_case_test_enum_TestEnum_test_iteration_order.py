# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_iteration_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Season(Enum):
        SUMMER = 2
        WINTER = 4
        AUTUMN = 3
        SPRING = 1
    self.assertEqual(list(Season), [Season.SUMMER, Season.WINTER, Season.AUTUMN, Season.SPRING])
