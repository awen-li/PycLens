# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_flowinfo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(OverflowError, socket.getnameinfo, (socket_helper.HOSTv6, 0, 4294967295), 0)
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
        self.assertRaises(OverflowError, s.bind, (socket_helper.HOSTv6, 0, -10))
