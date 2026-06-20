# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_check_hostname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    (client_context, server_context, hostname) = testing_context()
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            cert = s.getpeercert()
            self.assertTrue(cert, "Can't get peer certificate.")
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname='invalid') as s:
            with self.assertRaisesRegex(ssl.CertificateError, "Hostname mismatch, certificate is not valid for 'invalid'."):
                s.connect((HOST, server.port))
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with socket.socket() as s:
            with self.assertRaisesRegex(ValueError, 'check_hostname requires server_hostname'):
                client_context.wrap_socket(s)
