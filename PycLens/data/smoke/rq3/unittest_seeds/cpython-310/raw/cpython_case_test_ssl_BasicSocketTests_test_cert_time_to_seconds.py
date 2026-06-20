# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_cert_time_to_seconds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    timestring = 'Jan  5 09:34:43 2018 GMT'
    ts = 1515144883.0
    self.cert_time_ok(timestring, ts)
    self.assertEqual(ssl.cert_time_to_seconds(cert_time=timestring), ts)
    self.cert_time_ok('Jan 05 09:34:43 2018 GMT', ts)
    self.cert_time_ok('JaN  5 09:34:43 2018 GmT', ts)
    self.cert_time_fail('Jan  5 09:34 2018 GMT')
    self.cert_time_fail('Jan  5 09:34:43 2018')
    self.cert_time_fail('Jan  5 09:34:43 2018 UTC')
    self.cert_time_fail('Jan 35 09:34:43 2018 GMT')
    self.cert_time_fail('Jon  5 09:34:43 2018 GMT')
    self.cert_time_fail('Jan  5 24:00:00 2018 GMT')
    self.cert_time_fail('Jan  5 09:60:43 2018 GMT')
    newyear_ts = 1230768000.0
    self.cert_time_ok('Dec 31 23:59:60 2008 GMT', newyear_ts)
    self.cert_time_ok('Jan  1 00:00:00 2009 GMT', newyear_ts)
    self.cert_time_ok('Jan  5 09:34:59 2018 GMT', 1515144899)
    self.cert_time_ok('Jan  5 09:34:60 2018 GMT', 1515144900)
    self.cert_time_ok('Jan  5 09:34:61 2018 GMT', 1515144901)
    self.cert_time_fail('Jan  5 09:34:62 2018 GMT')
    self.cert_time_ok('Dec 31 23:59:59 9999 GMT', 253402300799.0)
