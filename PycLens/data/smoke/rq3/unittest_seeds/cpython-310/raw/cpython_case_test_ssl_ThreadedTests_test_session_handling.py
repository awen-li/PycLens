# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_session_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    (client_context2, _, _) = testing_context()
    client_context.maximum_version = ssl.TLSVersion.TLSv1_2
    client_context2.maximum_version = ssl.TLSVersion.TLSv1_2
    server = ThreadedEchoServer(context=server_context, chatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            self.assertEqual(s.session, None)
            self.assertEqual(s.session_reused, None)
            s.connect((HOST, server.port))
            session = s.session
            self.assertTrue(session)
            with self.assertRaises(TypeError) as e:
                s.session = object
            self.assertEqual(str(e.exception), 'Value is not a SSLSession.')
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            with self.assertRaises(ValueError) as e:
                s.session = session
            self.assertEqual(str(e.exception), 'Cannot set session after handshake.')
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.session = session
            s.connect((HOST, server.port))
            self.assertEqual(s.session.id, session.id)
            self.assertEqual(s.session, session)
            self.assertEqual(s.session_reused, True)
        with client_context2.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            with self.assertRaises(ValueError) as e:
                s.session = session
                s.connect((HOST, server.port))
            self.assertEqual(str(e.exception), 'Session refers to a different SSLContext.')
