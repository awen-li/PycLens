# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: InheritanceTest_test_dup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sock = socket.socket()
    with sock:
        newsock = sock.dup()
        sock.close()
        with newsock:
            self.assertEqual(newsock.get_inheritable(), False)
