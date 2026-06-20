# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: MultiPathServerTestCase_test_root_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = xmlrpclib.ServerProxy(URL + '/')
    self.assertEqual(p.test(), '/')
