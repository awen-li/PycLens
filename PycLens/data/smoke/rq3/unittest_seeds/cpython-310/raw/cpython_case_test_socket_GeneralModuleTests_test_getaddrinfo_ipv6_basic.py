# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_getaddrinfo_ipv6_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ((*_, sockaddr),) = socket.getaddrinfo('ff02::1de:c0:face:8D', 1234, socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    self.assertEqual(sockaddr, ('ff02::1de:c0:face:8d', 1234, 0, 0))
