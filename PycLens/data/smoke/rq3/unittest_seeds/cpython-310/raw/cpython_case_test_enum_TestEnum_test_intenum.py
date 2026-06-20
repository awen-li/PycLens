# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_intenum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class WeekDay(IntEnum):
        SUNDAY = 1
        MONDAY = 2
        TUESDAY = 3
        WEDNESDAY = 4
        THURSDAY = 5
        FRIDAY = 6
        SATURDAY = 7
    self.assertEqual(['a', 'b', 'c'][WeekDay.MONDAY], 'c')
    self.assertEqual([i for i in range(WeekDay.TUESDAY)], [0, 1, 2])
    lst = list(WeekDay)
    self.assertEqual(len(lst), len(WeekDay))
    self.assertEqual(len(WeekDay), 7)
    target = 'SUNDAY MONDAY TUESDAY WEDNESDAY THURSDAY FRIDAY SATURDAY'
    target = target.split()
    for (i, weekday) in enumerate(target, 1):
        e = WeekDay(i)
        self.assertEqual(e, i)
        self.assertEqual(int(e), i)
        self.assertEqual(e.name, weekday)
        self.assertIn(e, WeekDay)
        self.assertEqual(lst.index(e) + 1, i)
        self.assertTrue(0 < e < 8)
        self.assertIs(type(e), WeekDay)
        self.assertIsInstance(e, int)
        self.assertIsInstance(e, Enum)
