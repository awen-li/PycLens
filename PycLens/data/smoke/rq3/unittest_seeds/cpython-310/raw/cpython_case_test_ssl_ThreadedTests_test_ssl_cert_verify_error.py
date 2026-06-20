# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_ssl_cert_verify_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    server_context.load_cert_chain(SIGNED_CERTFILE)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with context.wrap_socket(socket.socket(), server_hostname=SIGNED_CERTFILE_HOSTNAME) as s:
            try:
                s.connect((HOST, server.port))
            except ssl.SSLError as e:
                msg = 'unable to get local issuer certificate'
                self.assertIsInstance(e, ssl.SSLCertVerificationError)
                self.assertEqual(e.verify_code, 20)
                self.assertEqual(e.verify_message, msg)
                self.assertIn(msg, repr(e))
                self.assertIn('certificate verify failed', repr(e))
