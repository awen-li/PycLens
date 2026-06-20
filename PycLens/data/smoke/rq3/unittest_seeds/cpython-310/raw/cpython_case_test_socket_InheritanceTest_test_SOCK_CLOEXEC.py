# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: InheritanceTest_test_SOCK_CLOEXEC

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM | socket.SOCK_CLOEXEC) as s:
        self.assertEqual(s.type, socket.SOCK_STREAM)
        self.assertFalse(s.get_inheritable())
