# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_tls_unique_channel_binding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    (client_context, server_context, hostname) = testing_context()
    server = ThreadedEchoServer(context=server_context, chatty=True, connectionchatty=False)
    with server:
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            cb_data = s.get_channel_binding('tls-unique')
            if support.verbose:
                sys.stdout.write(' got channel binding data: {0!r}\n'.format(cb_data))
            self.assertIsNotNone(cb_data)
            if s.version() == 'TLSv1.3':
                self.assertEqual(len(cb_data), 48)
            else:
                self.assertEqual(len(cb_data), 12)
            s.write(b'CB tls-unique\n')
            peer_data_repr = s.read().strip()
            self.assertEqual(peer_data_repr, repr(cb_data).encode('us-ascii'))
        with client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((HOST, server.port))
            new_cb_data = s.get_channel_binding('tls-unique')
            if support.verbose:
                sys.stdout.write('got another channel binding data: {0!r}\n'.format(new_cb_data))
            self.assertNotEqual(cb_data, new_cb_data)
            self.assertIsNotNone(cb_data)
            if s.version() == 'TLSv1.3':
                self.assertEqual(len(cb_data), 48)
            else:
                self.assertEqual(len(cb_data), 12)
            s.write(b'CB tls-unique\n')
            peer_data_repr = s.read().strip()
            self.assertEqual(peer_data_repr, repr(new_cb_data).encode('us-ascii'))
