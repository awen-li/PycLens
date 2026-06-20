# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: InheritanceTest_test_socketpair

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (s1, s2) = socket.socketpair()
    self.addCleanup(s1.close)
    self.addCleanup(s2.close)
    self.assertEqual(s1.get_inheritable(), False)
    self.assertEqual(s2.get_inheritable(), False)
