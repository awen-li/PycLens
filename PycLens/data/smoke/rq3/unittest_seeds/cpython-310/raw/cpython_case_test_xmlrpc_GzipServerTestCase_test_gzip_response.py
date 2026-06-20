# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: GzipServerTestCase_test_gzip_response

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.Transport()
    p = xmlrpclib.ServerProxy(URL, transport=t)
    old = self.requestHandler.encode_threshold
    self.requestHandler.encode_threshold = None
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    a = t.response_length
    self.requestHandler.encode_threshold = 0
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    p('close')()
    b = t.response_length
    self.requestHandler.encode_threshold = old
    self.assertTrue(a > b)
