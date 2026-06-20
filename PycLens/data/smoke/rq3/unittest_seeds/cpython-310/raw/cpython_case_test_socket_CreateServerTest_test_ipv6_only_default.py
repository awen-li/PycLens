# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: CreateServerTest_test_ipv6_only_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.create_server(('::1', 0), family=socket.AF_INET6) as sock:
        assert sock.getsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY)
