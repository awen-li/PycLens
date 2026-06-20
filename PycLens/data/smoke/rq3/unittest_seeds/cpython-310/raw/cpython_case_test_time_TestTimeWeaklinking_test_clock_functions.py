# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestTimeWeaklinking_test_clock_functions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import sysconfig
    import platform
    config_vars = sysconfig.get_config_vars()
    var_name = 'HAVE_CLOCK_GETTIME'
    if var_name not in config_vars or not config_vars[var_name]:
        raise unittest.SkipTest(f'{var_name} is not available')
    mac_ver = tuple((int(x) for x in platform.mac_ver()[0].split('.')))
    clock_names = ['CLOCK_MONOTONIC', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns', 'clock_getres']
    if mac_ver >= (10, 12):
        for name in clock_names:
            self.assertTrue(hasattr(time, name), f'time.{name} is not available')
    else:
        for name in clock_names:
            self.assertFalse(hasattr(time, name), f'time.{name} is available')
