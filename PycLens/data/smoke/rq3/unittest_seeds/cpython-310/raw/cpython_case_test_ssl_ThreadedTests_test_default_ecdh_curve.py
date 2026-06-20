# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_default_ecdh_curve

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    client_context.maximum_version = ssl.TLSVersion.TLSv1_2
    with ThreadedEchoServer(context=server_context) as server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            self.assertIn('ECDH', s.cipher()[0])
