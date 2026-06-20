# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_issue16464

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = self.start_server([(200, [], b'any'), (200, [], b'any')])
    opener = urllib.request.build_opener()
    request = urllib.request.Request('http://localhost:%s' % handler.port)
    self.assertEqual(None, request.data)
    opener.open(request, '1'.encode('us-ascii'))
    self.assertEqual(b'1', request.data)
    self.assertEqual('1', request.get_header('Content-length'))
    opener.open(request, '1234567890'.encode('us-ascii'))
    self.assertEqual(b'1234567890', request.data)
    self.assertEqual('10', request.get_header('Content-length'))
