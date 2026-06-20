# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntStrDigitLimitsTests_test_denial_of_service_prevented_str_to_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    maxdigits = sys.get_int_max_str_digits()
    assert maxdigits < 100000, maxdigits
    get_time = time.process_time
    if get_time() <= 0:
        get_time = time.monotonic
    digits = 133700
    huge = '8' * digits
    with support.adjust_int_max_str_digits(digits):
        start = get_time()
        int(huge)
    seconds_to_convert = get_time() - start
    if seconds_to_convert < 1 / 64:
        raise unittest.SkipTest(f'"slow" conversion took only {seconds_to_convert} seconds.')
    with support.adjust_int_max_str_digits(digits - 1):
        with self.assertRaises(ValueError) as err:
            start = get_time()
            int(huge)
        seconds_to_fail_huge = get_time() - start
    self.assertIn('conversion', str(err.exception))
    self.assertLessEqual(seconds_to_fail_huge, seconds_to_convert / 2)
    extra_huge = '7' * 1200000
    with self.assertRaises(ValueError) as err:
        start = get_time()
        int(extra_huge)
    seconds_to_fail_extra_huge = get_time() - start
    self.assertIn('conversion', str(err.exception))
    self.assertLessEqual(seconds_to_fail_extra_huge, seconds_to_convert / 2)
