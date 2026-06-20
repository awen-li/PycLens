# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_fd_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    start = os_helper.fd_count()
    fd = os.open(__file__, os.O_RDONLY)
    try:
        more = os_helper.fd_count()
    finally:
        os.close(fd)
    self.assertEqual(more - start, 1)
