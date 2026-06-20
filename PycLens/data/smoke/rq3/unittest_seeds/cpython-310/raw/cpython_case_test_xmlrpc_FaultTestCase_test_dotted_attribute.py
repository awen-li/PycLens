# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: FaultTestCase_test_dotted_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(AttributeError, xmlrpc.server.resolve_dotted_attribute, str, '__add')
    self.assertTrue(xmlrpc.server.resolve_dotted_attribute(str, 'title'))
