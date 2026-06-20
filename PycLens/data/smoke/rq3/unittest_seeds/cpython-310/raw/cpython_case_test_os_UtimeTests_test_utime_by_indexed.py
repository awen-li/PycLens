# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: UtimeTests_test_utime_by_indexed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def set_time(filename, ns):
        (atime_ns, mtime_ns) = ns
        atime = self.ns_to_sec(atime_ns)
        mtime = self.ns_to_sec(mtime_ns)
        os.utime(filename, (atime, mtime))
    self._test_utime(set_time)
