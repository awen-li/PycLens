# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_ignore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Period(timedelta, Enum):
        """
            different lengths of time
            """

        def __new__(cls, value, period):
            obj = timedelta.__new__(cls, value)
            obj._value_ = value
            obj.period = period
            return obj
        _ignore_ = 'Period i'
        Period = vars()
        for i in range(13):
            Period['month_%d' % i] = (i * 30, 'month')
        for i in range(53):
            Period['week_%d' % i] = (i * 7, 'week')
        for i in range(32):
            Period['day_%d' % i] = (i, 'day')
        OneDay = day_1
        OneWeek = week_1
        OneMonth = month_1
    self.assertFalse(hasattr(Period, '_ignore_'))
    self.assertFalse(hasattr(Period, 'Period'))
    self.assertFalse(hasattr(Period, 'i'))
    self.assertTrue(isinstance(Period.day_1, timedelta))
    self.assertTrue(Period.month_1 is Period.day_30)
    self.assertTrue(Period.week_4 is Period.day_28)
