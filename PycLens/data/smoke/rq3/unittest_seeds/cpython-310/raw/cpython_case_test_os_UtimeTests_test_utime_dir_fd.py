# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: UtimeTests_test_utime_dir_fd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def set_time(filename, ns):
        (dirname, name) = os.path.split(filename)
        with os_helper.open_dir_fd(dirname) as dirfd:
            os.utime(name, dir_fd=dirfd, ns=ns)
    self._test_utime(set_time)
