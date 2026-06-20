# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TimesTests_test_times

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    times = os.times()
    self.assertIsInstance(times, os.times_result)
    for field in ('user', 'system', 'children_user', 'children_system', 'elapsed'):
        value = getattr(times, field)
        self.assertIsInstance(value, float)
    if os.name == 'nt':
        self.assertEqual(times.children_user, 0)
        self.assertEqual(times.children_system, 0)
        self.assertEqual(times.elapsed, 0)
