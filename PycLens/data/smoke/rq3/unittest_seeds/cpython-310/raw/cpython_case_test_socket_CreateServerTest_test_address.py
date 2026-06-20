# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socket.py
# case: CreateServerTest_test_address

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    port = socket_helper.find_unused_port()
    with socket.create_server(('127.0.0.1', port)) as sock:
        self.assertEqual(sock.getsockname()[0], '127.0.0.1')
        self.assertEqual(sock.getsockname()[1], port)
    if socket_helper.IPV6_ENABLED:
        with socket.create_server(('::1', port), family=socket.AF_INET6) as sock:
            self.assertEqual(sock.getsockname()[0], '::1')
            self.assertEqual(sock.getsockname()[1], port)
