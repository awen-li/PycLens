# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_redirection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_response = b'We got here...'
    responses = [(302, [('Location', 'http://localhost:%(port)s/somewhere_else')], ''), (200, [], expected_response)]
    handler = self.start_server(responses)
    data = self.urlopen('http://localhost:%s/' % handler.port)
    self.assertEqual(data, expected_response)
    self.assertEqual(handler.requests, ['/', '/somewhere_else'])
