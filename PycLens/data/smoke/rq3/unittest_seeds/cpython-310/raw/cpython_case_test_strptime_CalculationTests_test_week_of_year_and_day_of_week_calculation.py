# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: CalculationTests_test_week_of_year_and_day_of_week_calculation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test_helper(ymd_tuple, test_reason):
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
    test_helper((1901, 1, 3), 'week 0')
    test_helper((1901, 1, 8), 'common case')
    test_helper((1901, 1, 13), 'day on Sunday')
    test_helper((1901, 1, 14), 'day on Monday')
    test_helper((1905, 1, 1), 'Jan 1 on Sunday')
    test_helper((1906, 1, 1), 'Jan 1 on Monday')
    test_helper((1906, 1, 7), 'first Sunday in a year starting on Monday')
    test_helper((1905, 12, 31), 'Dec 31 on Sunday')
    test_helper((1906, 12, 31), 'Dec 31 on Monday')
    test_helper((2008, 12, 29), 'Monday in the last week of the year')
    test_helper((2008, 12, 22), 'Monday in the second-to-last week of the year')
    test_helper((1978, 10, 23), 'randomly chosen date')
    test_helper((2004, 12, 18), 'randomly chosen date')
    test_helper((1978, 10, 23), 'year starting and ending on Monday while date not on Sunday or Monday')
    test_helper((1917, 12, 17), 'year starting and ending on Monday with a Monday not at the beginning or end of the year')
    test_helper((1917, 12, 31), 'Dec 31 on Monday with year starting and ending on Monday')
    test_helper((2007, 1, 7), 'First Sunday of 2007')
    test_helper((2007, 1, 14), 'Second Sunday of 2007')
    test_helper((2006, 12, 31), 'Last Sunday of 2006')
    test_helper((2006, 12, 24), 'Second to last Sunday of 2006')
