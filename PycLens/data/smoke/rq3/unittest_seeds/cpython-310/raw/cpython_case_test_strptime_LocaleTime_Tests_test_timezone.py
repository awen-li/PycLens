# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: LocaleTime_Tests_test_timezone

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    timezone = time.strftime('%Z', self.time_tuple).lower()
    if timezone:
        self.assertTrue(timezone in self.LT_ins.timezone[0] or timezone in self.LT_ins.timezone[1], 'timezone %s not found in %s' % (timezone, self.LT_ins.timezone))
