# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_min_max_version_mismatch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    server_context.maximum_version = ssl.TLSVersion.TLSv1_2
    server_context.minimum_version = ssl.TLSVersion.TLSv1_2
    client_context.maximum_version = ssl.TLSVersion.TLSv1
    client_context.minimum_version = ssl.TLSVersion.TLSv1
    seclevel_workaround(client_context, server_context)
    with ThreadedEchoServer(context=server_context) as server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            with self.assertRaises(ssl.SSLError) as e:
                s.connect((HOST, server.port))
            self.assertIn('alert', str(e.exception))
