# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_getpeercert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    (client_context, server_context, hostname) = testing_context()
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), do_handshake_on_connect=False, server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            with self.assertRaises(ValueError):
                s.getpeercert()
            s.do_handshake()
            cert = s.getpeercert()
            self.assertTrue(cert, "Can't get peer certificate.")
            cipher = s.cipher()
            if support.verbose:
                sys.stdout.write(pprint.pformat(cert) + '\n')
                sys.stdout.write('Connection cipher is ' + str(cipher) + '.\n')
            if 'subject' not in cert:
                self.fail('No subject field in certificate: %s.' % pprint.pformat(cert))
            if (('organizationName', 'Python Software Foundation'),) not in cert['subject']:
                self.fail("Missing or invalid 'organizationName' field in certificate subject; should be 'Python Software Foundation'.")
            self.assertIn('notBefore', cert)
            self.assertIn('notAfter', cert)
            before = ssl.cert_time_to_seconds(cert['notBefore'])
            after = ssl.cert_time_to_seconds(cert['notAfter'])
            self.assertLess(before, after)
