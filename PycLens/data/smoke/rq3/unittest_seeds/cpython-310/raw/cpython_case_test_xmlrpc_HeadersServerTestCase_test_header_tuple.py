# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: HeadersServerTestCase_test_header_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = xmlrpclib.ServerProxy(URL, headers=(('X-Test', 'foo'),))
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    headers = self.RequestHandler.test_headers
    self.assertContainsAdditionalHeaders(headers, {'X-Test': 'foo'})
