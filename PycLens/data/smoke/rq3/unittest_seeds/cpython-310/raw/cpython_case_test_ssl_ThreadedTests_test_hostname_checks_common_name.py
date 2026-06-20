# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_hostname_checks_common_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    assert client_context.hostname_checks_common_name
    client_context.hostname_checks_common_name = False
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
    (client_context, server_context, hostname) = testing_context(NOSANFILE)
    client_context.hostname_checks_common_name = False
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            with self.assertRaises(ssl.SSLCertVerificationError):
                s.connect((HOST, server.port))
