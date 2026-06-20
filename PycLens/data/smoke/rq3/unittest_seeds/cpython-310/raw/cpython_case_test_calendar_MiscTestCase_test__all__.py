# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_calendar.py
# case: MiscTestCase_test__all__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    not_exported = {'mdays', 'January', 'February', 'EPOCH', 'different_locale', 'c', 'prweek', 'week', 'format', 'formatstring', 'main', 'monthlen', 'prevmonth', 'nextmonth'}
    support.check__all__(self, calendar, not_exported=not_exported)
