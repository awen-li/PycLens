# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_response = b'pycon 2008...'
    handler = self.start_server([(200, [], expected_response)])
    data = urllib.request.urlopen('http://localhost:%s' % handler.port)
    for line in data:
        self.assertEqual(line, expected_response)
