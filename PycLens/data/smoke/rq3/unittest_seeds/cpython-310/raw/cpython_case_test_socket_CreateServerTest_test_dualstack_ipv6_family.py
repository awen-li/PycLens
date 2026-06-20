# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: CreateServerTest_test_dualstack_ipv6_family

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.create_server(('::1', 0), family=socket.AF_INET6, dualstack_ipv6=True) as sock:
        self.assertEqual(sock.family, socket.AF_INET6)
