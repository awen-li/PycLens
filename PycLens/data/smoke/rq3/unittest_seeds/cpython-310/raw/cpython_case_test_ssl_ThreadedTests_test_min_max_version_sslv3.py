# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_min_max_version_sslv3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    server_context.minimum_version = ssl.TLSVersion.SSLv3
    client_context.minimum_version = ssl.TLSVersion.SSLv3
    client_context.maximum_version = ssl.TLSVersion.SSLv3
    seclevel_workaround(client_context, server_context)
    with ThreadedEchoServer(context=server_context) as server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            self.assertEqual(s.version(), 'SSLv3')
