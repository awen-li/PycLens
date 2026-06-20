# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: CalculationTests_test_julian_calculation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    format_string = '%Y %m %d %H %M %S %w %Z'
    result = _strptime._strptime_time(time.strftime(format_string, self.time_tuple), format_string)
    self.assertTrue(result.tm_yday == self.time_tuple.tm_yday, 'Calculation of tm_yday failed; %s != %s' % (result.tm_yday, self.time_tuple.tm_yday))
