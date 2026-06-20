# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: HelperTestCase_test_escape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(xmlrpclib.escape('a&b'), 'a&amp;b')
    self.assertEqual(xmlrpclib.escape('a<b'), 'a&lt;b')
    self.assertEqual(xmlrpclib.escape('a>b'), 'a&gt;b')
