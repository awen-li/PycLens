# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: GeneralModuleTests_test_getnameinfo_ipv6_scopeid_numeric

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ifindex = 42
    sockaddr = ('ff02::1de:c0:face:8D', 1234, 0, ifindex)
    nameinfo = socket.getnameinfo(sockaddr, socket.NI_NUMERICHOST | socket.NI_NUMERICSERV)
    self.assertEqual(nameinfo, ('ff02::1de:c0:face:8d%' + str(ifindex), '1234'))
