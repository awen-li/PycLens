# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_kqueue.py
# case: TestKQueue_test_fd_non_inheritable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    kqueue = select.kqueue()
    self.addCleanup(kqueue.close)
    self.assertEqual(os.get_inheritable(kqueue.fileno()), False)
