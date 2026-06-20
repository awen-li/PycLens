# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_regrtest.py
# case: TestUtils_test_format_duration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(utils.format_duration(0), '0 ms')
    self.assertEqual(utils.format_duration(1e-09), '1 ms')
    self.assertEqual(utils.format_duration(0.01), '10 ms')
    self.assertEqual(utils.format_duration(1.5), '1.5 sec')
    self.assertEqual(utils.format_duration(1), '1.0 sec')
    self.assertEqual(utils.format_duration(2 * 60), '2 min')
    self.assertEqual(utils.format_duration(2 * 60 + 1), '2 min 1 sec')
    self.assertEqual(utils.format_duration(3 * 3600), '3 hour')
    self.assertEqual(utils.format_duration(3 * 3600 + 2 * 60 + 1), '3 hour 2 min')
    self.assertEqual(utils.format_duration(3 * 3600 + 1), '3 hour 1 sec')
