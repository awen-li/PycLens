# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: CalculationTests_test_gregorian_calculation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    format_string = '%Y %H %M %S %w %j %Z'
    result = _strptime._strptime_time(time.strftime(format_string, self.time_tuple), format_string)
    self.assertTrue(result.tm_year == self.time_tuple.tm_year and result.tm_mon == self.time_tuple.tm_mon and (result.tm_mday == self.time_tuple.tm_mday), 'Calculation of Gregorian date failed; %s-%s-%s != %s-%s-%s' % (result.tm_year, result.tm_mon, result.tm_mday, self.time_tuple.tm_year, self.time_tuple.tm_mon, self.time_tuple.tm_mday))
