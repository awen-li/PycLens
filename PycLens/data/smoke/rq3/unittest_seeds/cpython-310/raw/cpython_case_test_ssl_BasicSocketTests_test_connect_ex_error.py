# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_connect_ex_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = socket.socket(socket.AF_INET)
    self.addCleanup(server.close)
    port = socket_helper.bind_port(server)
    s = test_wrap_socket(socket.socket(socket.AF_INET), cert_reqs=ssl.CERT_REQUIRED)
    self.addCleanup(s.close)
    rc = s.connect_ex((HOST, port))
    errors = (errno.ECONNREFUSED, errno.EHOSTUNREACH, errno.ETIMEDOUT, errno.EWOULDBLOCK)
    self.assertIn(rc, errors)
