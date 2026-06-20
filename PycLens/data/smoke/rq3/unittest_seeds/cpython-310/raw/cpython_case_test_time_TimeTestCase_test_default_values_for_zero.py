# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_default_values_for_zero

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = '2000 01 01 00 00 00 1 001'
    with warnings_helper.check_warnings():
        result = time.strftime('%Y %m %d %H %M %S %w %j', (2000,) + (0,) * 8)
    self.assertEqual(expected, result)
