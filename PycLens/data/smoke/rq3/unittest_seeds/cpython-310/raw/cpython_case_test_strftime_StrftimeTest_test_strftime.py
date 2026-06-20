# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strftime.py
# case: StrftimeTest_test_strftime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    now = time.time()
    self._update_variables(now)
    self.strftest1(now)
    self.strftest2(now)
    if support.verbose:
        print('Strftime test, platform: %s, Python version: %s' % (sys.platform, sys.version.split()[0]))
    for j in range(-5, 5):
        for i in range(25):
            arg = now + (i + j * 100) * 23 * 3603
            self._update_variables(arg)
            self.strftest1(arg)
            self.strftest2(arg)
