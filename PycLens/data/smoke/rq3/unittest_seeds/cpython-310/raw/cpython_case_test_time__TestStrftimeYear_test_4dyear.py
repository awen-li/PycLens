# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: _TestStrftimeYear_test_4dyear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self._format == '%04d':
        self.test_year('%04d')
    else:

        def year4d(y):
            return time.strftime('%4Y', (y,) + (0,) * 8)
        self.test_year('%04d', func=year4d)
