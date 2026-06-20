# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_docxmlrpc.py
# case: DocXMLRPCHTTPGETServer_test_invalid_get_response

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.request('GET', '/spam')
    response = self.client.getresponse()
    self.assertEqual(response.status, 404)
    self.assertEqual(response.getheader('Content-type'), 'text/plain')
    response.read()
