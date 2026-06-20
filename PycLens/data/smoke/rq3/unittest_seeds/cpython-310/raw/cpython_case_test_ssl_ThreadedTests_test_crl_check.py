# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_crl_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    (client_context, server_context, hostname) = testing_context()
    tf = getattr(ssl, 'VERIFY_X509_TRUSTED_FIRST', 0)
    self.assertEqual(client_context.verify_flags, ssl.VERIFY_DEFAULT | tf)
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            cert = s.getpeercert()
            self.assertTrue(cert, "Can't get peer certificate.")
    client_context.verify_flags |= ssl.VERIFY_CRL_CHECK_LEAF
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            with self.assertRaisesRegex(ssl.SSLError, 'certificate verify failed'):
                s.connect((HOST, server.port))
    client_context.load_verify_locations(CRLFILE)
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            cert = s.getpeercert()
            self.assertTrue(cert, "Can't get peer certificate.")
