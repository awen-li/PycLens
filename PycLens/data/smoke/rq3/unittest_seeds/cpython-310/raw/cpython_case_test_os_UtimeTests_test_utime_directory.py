# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: UtimeTests_test_utime_directory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def set_time(filename, ns):
        os.utime(filename, ns=ns)
    self._test_utime(set_time, filename=self.dirname)
