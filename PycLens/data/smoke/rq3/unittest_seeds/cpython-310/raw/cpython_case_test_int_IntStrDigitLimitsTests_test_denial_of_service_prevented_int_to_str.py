# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntStrDigitLimitsTests_test_denial_of_service_prevented_int_to_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    maxdigits = sys.get_int_max_str_digits()
    assert maxdigits < 50000, maxdigits
    get_time = time.process_time
    if get_time() <= 0:
        get_time = time.monotonic
    huge_int = int(f"0x{'c' * 65000}", base=16)
    digits = 78268
    with support.adjust_int_max_str_digits(digits):
        start = get_time()
        huge_decimal = str(huge_int)
    seconds_to_convert = get_time() - start
    self.assertEqual(len(huge_decimal), digits)
    if seconds_to_convert < 1 / 64:
        raise unittest.SkipTest(f'"slow" conversion took only {seconds_to_convert} seconds.')
    with support.adjust_int_max_str_digits(int(0.995 * digits)):
        with self.assertRaises(ValueError) as err:
            start = get_time()
            str(huge_int)
        seconds_to_fail_huge = get_time() - start
    self.assertIn('conversion', str(err.exception))
    self.assertLessEqual(seconds_to_fail_huge, seconds_to_convert / 2)
    extra_huge_int = int(f"0x{'c' * 500000}", base=16)
    with self.assertRaises(ValueError) as err:
        start = get_time()
        str(extra_huge_int)
    seconds_to_fail_extra_huge = get_time() - start
    self.assertIn('conversion', str(err.exception))
    self.assertLess(seconds_to_fail_extra_huge, seconds_to_convert / 2)
