# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_echo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    (client_context, server_context, hostname) = testing_context()
    with self.subTest(client=ssl.PROTOCOL_TLS_CLIENT, server=ssl.PROTOCOL_TLS_SERVER):
        server_params_test(client_context=client_context, server_context=server_context, chatty=True, connectionchatty=True, sni_name=hostname)
    client_context.check_hostname = False
    with self.subTest(client=ssl.PROTOCOL_TLS_SERVER, server=ssl.PROTOCOL_TLS_CLIENT):
        with self.assertRaises(ssl.SSLError) as e:
            server_params_test(client_context=server_context, server_context=client_context, chatty=True, connectionchatty=True, sni_name=hostname)
        self.assertIn('Cannot create a client socket with a PROTOCOL_TLS_SERVER context', str(e.exception))
    with self.subTest(client=ssl.PROTOCOL_TLS_SERVER, server=ssl.PROTOCOL_TLS_SERVER):
        with self.assertRaises(ssl.SSLError) as e:
            server_params_test(client_context=server_context, server_context=server_context, chatty=True, connectionchatty=True)
        self.assertIn('Cannot create a client socket with a PROTOCOL_TLS_SERVER context', str(e.exception))
    with self.subTest(client=ssl.PROTOCOL_TLS_CLIENT, server=ssl.PROTOCOL_TLS_CLIENT):
        with self.assertRaises(ssl.SSLError) as e:
            server_params_test(client_context=server_context, server_context=client_context, chatty=True, connectionchatty=True)
        self.assertIn('Cannot create a client socket with a PROTOCOL_TLS_SERVER context', str(e.exception))
