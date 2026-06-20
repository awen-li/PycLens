# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_cert_time_to_seconds_locale

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def local_february_name():
        return time.strftime('%b', (1, 2, 3, 4, 5, 6, 0, 0, 0))
    if local_february_name().lower() == 'feb':
        self.skipTest('locale-specific month name needs to be different from C locale')
    self.cert_time_ok('Feb  9 00:00:00 2007 GMT', 1170979200.0)
    self.cert_time_fail(local_february_name() + '  9 00:00:00 2007 GMT')
