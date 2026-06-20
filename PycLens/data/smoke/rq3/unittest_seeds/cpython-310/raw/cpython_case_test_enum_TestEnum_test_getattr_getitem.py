# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_getattr_getitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Period(Enum):
        morning = 1
        noon = 2
        evening = 3
        night = 4
    self.assertIs(Period(2), Period.noon)
    self.assertIs(getattr(Period, 'night'), Period.night)
    self.assertIs(Period['morning'], Period.morning)
