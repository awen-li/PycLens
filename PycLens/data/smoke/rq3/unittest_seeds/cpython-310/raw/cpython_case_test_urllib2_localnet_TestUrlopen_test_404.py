# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_404

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_response = b'Bad bad bad...'
    handler = self.start_server([(404, [], expected_response)])
    try:
        self.urlopen('http://localhost:%s/weeble' % handler.port)
    except urllib.error.URLError as f:
        data = f.read()
        f.close()
    else:
        self.fail('404 should raise URLError')
    self.assertEqual(data, expected_response)
    self.assertEqual(handler.requests, ['/weeble'])
