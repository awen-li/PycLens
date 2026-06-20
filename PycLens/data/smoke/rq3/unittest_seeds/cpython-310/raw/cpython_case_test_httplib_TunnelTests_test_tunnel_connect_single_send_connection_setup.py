# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: TunnelTests_test_tunnel_connect_single_send_connection_setup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch.object(self.conn, 'send') as mock_send:
        self.conn.set_tunnel('destination.com')
        self.conn.connect()
        self.conn.request('GET', '/')
    mock_send.assert_called()
    self.assertGreater(len(mock_send.mock_calls), 1, msg=f'unexpected number of send calls: {mock_send.mock_calls}')
    proxy_setup_data_sent = mock_send.mock_calls[0][1][0]
    self.assertIn(b'CONNECT destination.com', proxy_setup_data_sent)
    self.assertTrue(proxy_setup_data_sent.endswith(b'\r\n\r\n'), msg=f'unexpected proxy data sent {proxy_setup_data_sent!r}')
