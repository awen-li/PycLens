# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_cert_time_to_seconds_timezone

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.cert_time_ok('May  9 00:00:00 2007 GMT', 1178668800.0)
    self.cert_time_ok('Jan  5 09:34:43 2018 GMT', 1515144883.0)
