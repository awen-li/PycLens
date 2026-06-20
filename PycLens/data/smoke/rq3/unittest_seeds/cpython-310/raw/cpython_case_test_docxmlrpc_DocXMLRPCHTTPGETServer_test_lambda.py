# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_docxmlrpc.py
# case: DocXMLRPCHTTPGETServer_test_lambda

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.request('GET', '/')
    response = self.client.getresponse()
    self.assertIn(b'<dl><dt><a name="-&lt;lambda&gt;"><strong>&lt;lambda&gt;</strong></a>(x, y)</dt></dl>', response.read())
