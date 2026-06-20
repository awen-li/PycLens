# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: UtimeTests_test_utime_current_old

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def set_time(filename):
        os.utime(self.fname, None)
    self._test_utime_current(set_time)
