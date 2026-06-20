# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: CGIHTTPServerTestCase_test_accept

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    browser_accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    tests = (((('Accept', browser_accept),), browser_accept), ((), ''), ((('Accept', 'text/html'), ('ACCEPT', 'text/plain')), 'text/html,text/plain'))
    for (headers, expected) in tests:
        headers = OrderedDict(headers)
        with self.subTest(headers):
            res = self.request('/cgi-bin/file6.py', 'GET', headers=headers)
            self.assertEqual(http.HTTPStatus.OK, res.status)
            expected = f'HTTP_ACCEPT={expected}'.encode('ascii')
            self.assertIn(expected, res.read())
