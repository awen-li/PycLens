# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: OutputTestCase_test_yeardatescalendar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def shrink(cal):
        return [[[' '.join(('{:02d}/{:02d}/{}'.format(d.month, d.day, str(d.year)[-2:]) for d in z)) for z in y] for y in x] for x in cal]
    self.assertEqual(shrink(calendar.Calendar().yeardatescalendar(2004)), result_2004_dates)
