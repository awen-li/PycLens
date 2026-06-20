# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HeaderTests_test_parse_all_octets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    body = b"HTTP/1.1 200 OK\r\n!#$%&'*+-.^_`|~: value\r\nVCHAR: " + bytes(range(33, 126 + 1)) + b'\r\nobs-text: ' + bytes(range(128, 255 + 1)) + b'\r\nobs-fold: text\r\n folded with space\r\n\tfolded with tab\r\nContent-Length: 0\r\n\r\n'
    sock = FakeSocket(body)
    resp = client.HTTPResponse(sock)
    resp.begin()
    self.assertEqual(resp.getheader('Content-Length'), '0')
    self.assertEqual(resp.msg['Content-Length'], '0')
    self.assertEqual(resp.getheader("!#$%&'*+-.^_`|~"), 'value')
    self.assertEqual(resp.msg["!#$%&'*+-.^_`|~"], 'value')
    vchar = ''.join(map(chr, range(33, 126 + 1)))
    self.assertEqual(resp.getheader('VCHAR'), vchar)
    self.assertEqual(resp.msg['VCHAR'], vchar)
    self.assertIsNotNone(resp.getheader('obs-text'))
    self.assertIn('obs-text', resp.msg)
    for folded in (resp.getheader('obs-fold'), resp.msg['obs-fold']):
        self.assertTrue(folded.startswith('text'))
        self.assertIn(' folded with space', folded)
        self.assertTrue(folded.endswith('folded with tab'))
