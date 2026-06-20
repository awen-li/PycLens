# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: CalculationTests_test_week_of_year_and_day_of_week_calculation_test_helper

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for year_week_format in ('%Y %W', '%Y %U', '%G %V'):
        if year_week_format in self._formats_excluded and ymd_tuple in self._ymd_excluded:
            return
        for weekday_format in ('%w', '%u', '%a', '%A'):
            format_string = year_week_format + ' ' + weekday_format
            with self.subTest(test_reason, date=ymd_tuple, format=format_string):
                dt_date = datetime_date(*ymd_tuple)
                strp_input = dt_date.strftime(format_string)
                strp_output = _strptime._strptime_time(strp_input, format_string)
                msg = '%r: %s != %s' % (strp_input, strp_output[7], dt_date.timetuple()[7])
                self.assertEqual(strp_output[:3], ymd_tuple, msg)
