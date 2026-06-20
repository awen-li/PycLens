# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_sending_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    handler = self.start_server()
    req = urllib.request.Request('http://localhost:%s/' % handler.port, headers={'Range': 'bytes=20-39'})
    with urllib.request.urlopen(req):
        pass
    self.assertEqual(handler.headers_received['Range'], 'bytes=20-39')
