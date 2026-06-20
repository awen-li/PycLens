# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_docxmlrpc.py
# case: DocXMLRPCHTTPGETServer_test_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.request('GET', '/')
    response = self.client.getresponse()
    docstring = b'' if sys.flags.optimize >= 2 else b'<dd><tt>Use&nbsp;function&nbsp;annotations.</tt></dd>'
    self.assertIn(b'<dl><dt><a name="-annotation"><strong>annotation</strong></a>(x: int)</dt>' + docstring + b'</dl>\n<dl><dt><a name="-method_annotation"><strong>method_annotation</strong></a>(x: bytes)</dt></dl>', response.read())
