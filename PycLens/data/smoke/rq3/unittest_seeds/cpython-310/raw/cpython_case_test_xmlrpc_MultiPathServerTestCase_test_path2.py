# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: MultiPathServerTestCase_test_path2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = xmlrpclib.ServerProxy(URL + '/foo/bar')
    self.assertEqual(p.add(6, 8), 6 + 8)
    self.assertRaises(xmlrpclib.Fault, p.pow, 6, 8)
