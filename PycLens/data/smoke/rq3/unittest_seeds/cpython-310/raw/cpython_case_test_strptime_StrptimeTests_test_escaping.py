# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strptime.py
# case: StrptimeTests_test_escaping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    need_escaping = '.^$*+?{}\\[]|)('
    self.assertTrue(_strptime._strptime_time(need_escaping, need_escaping))
