# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestSendfile_test_flags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        os.sendfile(self.sockno, self.fileno, 0, 4096, flags=os.SF_NODISKIO)
    except OSError as err:
        if err.errno not in (errno.EBUSY, errno.EAGAIN):
            raise
