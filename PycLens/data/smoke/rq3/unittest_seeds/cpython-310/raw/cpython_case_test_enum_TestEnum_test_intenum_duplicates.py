# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_intenum_duplicates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class WeekDay(IntEnum):
        SUNDAY = 1
        MONDAY = 2
        TUESDAY = TEUSDAY = 3
        WEDNESDAY = 4
        THURSDAY = 5
        FRIDAY = 6
        SATURDAY = 7
    self.assertIs(WeekDay.TEUSDAY, WeekDay.TUESDAY)
    self.assertEqual(WeekDay(3).name, 'TUESDAY')
    self.assertEqual([k for (k, v) in WeekDay.__members__.items() if v.name != k], ['TEUSDAY'])
