# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: KeepaliveServerTestCase2_test_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = xmlrpclib.ServerProxy(URL)
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    p('close')()
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    self.assertEqual(p.pow(6, 8), 6 ** 8)
    p('close')()
    self.assertEqual(len(self.RequestHandler.myRequests), 2)
    self.assertGreaterEqual(len(self.RequestHandler.myRequests[-1]), 2)
    self.assertGreaterEqual(len(self.RequestHandler.myRequests[-2]), 2)
