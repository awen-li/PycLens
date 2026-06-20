# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_check_hostname_idn

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    server_context.load_cert_chain(IDNSANSFILE)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_verify_locations(SIGNING_CA)
    idn_hostnames = [('könig.idn.pythontest.net', 'xn--knig-5qa.idn.pythontest.net'), ('xn--knig-5qa.idn.pythontest.net', 'xn--knig-5qa.idn.pythontest.net'), (b'xn--knig-5qa.idn.pythontest.net', 'xn--knig-5qa.idn.pythontest.net'), ('königsgäßchen.idna2003.pythontest.net', 'xn--knigsgsschen-lcb0w.idna2003.pythontest.net'), ('xn--knigsgsschen-lcb0w.idna2003.pythontest.net', 'xn--knigsgsschen-lcb0w.idna2003.pythontest.net'), (b'xn--knigsgsschen-lcb0w.idna2003.pythontest.net', 'xn--knigsgsschen-lcb0w.idna2003.pythontest.net'), ('xn--knigsgchen-b4a3dun.idna2008.pythontest.net', 'xn--knigsgchen-b4a3dun.idna2008.pythontest.net'), (b'xn--knigsgchen-b4a3dun.idna2008.pythontest.net', 'xn--knigsgchen-b4a3dun.idna2008.pythontest.net')]
    for (server_hostname, expected_hostname) in idn_hostnames:
        server = ThreadedEchoServer(context=server_context, chatty=True)
        with server:
            with context.wrap_socket(socket.socket(), server_hostname=server_hostname) as s:
                self.assertEqual(s.server_hostname, expected_hostname)
                s.connect((HOST, server.port))
                cert = s.getpeercert()
                self.assertEqual(s.server_hostname, expected_hostname)
                self.assertTrue(cert, "Can't get peer certificate.")
    server = ThreadedEchoServer(context=server_context, chatty=True)
    with server:
        with context.wrap_socket(socket.socket(), server_hostname='python.example.org') as s:
            with self.assertRaises(ssl.CertificateError):
                s.connect((HOST, server.port))
