# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_dump_big_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.maxsize > 2 ** 31 - 1:
        self.assertRaises(OverflowError, xmlrpclib.dumps, (int(2 ** 34),))
    xmlrpclib.dumps((xmlrpclib.MAXINT, xmlrpclib.MININT))
    self.assertRaises(OverflowError, xmlrpclib.dumps, (xmlrpclib.MAXINT + 1,))
    self.assertRaises(OverflowError, xmlrpclib.dumps, (xmlrpclib.MININT - 1,))

    def dummy_write(s):
        pass
    m = xmlrpclib.Marshaller()
    m.dump_int(xmlrpclib.MAXINT, dummy_write)
    m.dump_int(xmlrpclib.MININT, dummy_write)
    self.assertRaises(OverflowError, m.dump_int, xmlrpclib.MAXINT + 1, dummy_write)
    self.assertRaises(OverflowError, m.dump_int, xmlrpclib.MININT - 1, dummy_write)
