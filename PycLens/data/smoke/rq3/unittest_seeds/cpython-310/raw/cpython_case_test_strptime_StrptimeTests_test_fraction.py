# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_fraction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import datetime
    d = datetime.datetime(2012, 12, 20, 12, 34, 56, 78987)
    (tup, frac, _) = _strptime._strptime(str(d), format='%Y-%m-%d %H:%M:%S.%f')
    self.assertEqual(frac, d.microsecond)
