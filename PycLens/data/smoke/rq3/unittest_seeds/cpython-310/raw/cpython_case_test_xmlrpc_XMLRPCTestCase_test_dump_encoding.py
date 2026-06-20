# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_dump_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    value = {'key€¤': 'value€¤'}
    strg = xmlrpclib.dumps((value,), encoding='iso-8859-15')
    strg = "<?xml version='1.0' encoding='iso-8859-15'?>" + strg
    self.assertEqual(xmlrpclib.loads(strg)[0][0], value)
    strg = strg.encode('iso-8859-15', 'xmlcharrefreplace')
    self.assertEqual(xmlrpclib.loads(strg)[0][0], value)
    strg = xmlrpclib.dumps((value,), encoding='iso-8859-15', methodresponse=True)
    self.assertEqual(xmlrpclib.loads(strg)[0][0], value)
    strg = strg.encode('iso-8859-15', 'xmlcharrefreplace')
    self.assertEqual(xmlrpclib.loads(strg)[0][0], value)
    methodname = 'method€¤'
    strg = xmlrpclib.dumps((value,), encoding='iso-8859-15', methodname=methodname)
    self.assertEqual(xmlrpclib.loads(strg)[0][0], value)
    self.assertEqual(xmlrpclib.loads(strg)[1], methodname)
