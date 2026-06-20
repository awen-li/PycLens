# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: GzipServerTestCase_test_gzip_request

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.Transport()
    t.encode_threshold = None
    p = xmlrpclib.ServerProxy(URL, transport=t)
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    a = self.RequestHandler.content_length
    t.encode_threshold = 0
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    b = self.RequestHandler.content_length
    self.assertTrue(a > b)
    p('close')()
