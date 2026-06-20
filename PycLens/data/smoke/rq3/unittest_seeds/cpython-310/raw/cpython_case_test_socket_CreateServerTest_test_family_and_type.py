# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: CreateServerTest_test_family_and_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.create_server(('127.0.0.1', 0)) as sock:
        self.assertEqual(sock.family, socket.AF_INET)
        self.assertEqual(sock.type, socket.SOCK_STREAM)
    if socket_helper.IPV6_ENABLED:
        with socket.create_server(('::1', 0), family=socket.AF_INET6) as s:
            self.assertEqual(s.family, socket.AF_INET6)
            self.assertEqual(sock.type, socket.SOCK_STREAM)
