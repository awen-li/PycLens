# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: InheritanceTest_test_default_inheritable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket()
    with sock:
        self.assertEqual(sock.get_inheritable(), False)
