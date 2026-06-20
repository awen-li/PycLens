# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TestLocale_test_bug_3061

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        tmp = locale.setlocale(locale.LC_ALL, 'fr_FR')
    except locale.Error:
        self.skipTest('could not set locale.LC_ALL to fr_FR')
    time.strftime('%B', (2009, 2, 1, 0, 0, 0, 0, 0, 0))
