# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_200_with_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_response = b'pycon 2008...'
    handler = self.start_server([(200, [], expected_response)])
    data = self.urlopen('http://localhost:%s/bizarre' % handler.port, b'get=with_feeling')
    self.assertEqual(data, expected_response)
    self.assertEqual(handler.requests, ['/bizarre', b'get=with_feeling'])
