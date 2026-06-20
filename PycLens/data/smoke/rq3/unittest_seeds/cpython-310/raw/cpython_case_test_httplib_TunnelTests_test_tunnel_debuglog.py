# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: TunnelTests_test_tunnel_debuglog

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_header = 'X-Dummy: 1'
    response_text = 'HTTP/1.0 200 OK\r\n{}\r\n\r\n'.format(expected_header)
    self.conn.set_debuglevel(1)
    self.conn._create_connection = self._create_connection(response_text)
    self.conn.set_tunnel('destination.com')
    with support.captured_stdout() as output:
        self.conn.request('PUT', '/', '')
    lines = output.getvalue().splitlines()
    self.assertIn('header: {}'.format(expected_header), lines)
