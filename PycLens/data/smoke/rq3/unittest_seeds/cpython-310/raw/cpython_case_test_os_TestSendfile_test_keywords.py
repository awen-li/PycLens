# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestSendfile_test_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.sendfile(out_fd=self.sockno, in_fd=self.fileno, offset=0, count=4096)
    if self.SUPPORT_HEADERS_TRAILERS:
        os.sendfile(out_fd=self.sockno, in_fd=self.fileno, offset=0, count=4096, headers=(), trailers=(), flags=0)
