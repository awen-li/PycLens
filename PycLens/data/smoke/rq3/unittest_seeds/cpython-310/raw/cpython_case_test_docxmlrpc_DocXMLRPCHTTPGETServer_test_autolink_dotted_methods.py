# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_docxmlrpc.py
# case: DocXMLRPCHTTPGETServer_test_autolink_dotted_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.request('GET', '/')
    response = self.client.getresponse()
    self.assertIn(b'Try&nbsp;self.<strong>add</strong>,&nbsp;too.', response.read())
