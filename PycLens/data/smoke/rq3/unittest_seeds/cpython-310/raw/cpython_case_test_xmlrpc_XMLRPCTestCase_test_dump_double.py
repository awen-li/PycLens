# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_dump_double

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xmlrpclib.dumps((float(2 ** 34),))
    xmlrpclib.dumps((float(xmlrpclib.MAXINT), float(xmlrpclib.MININT)))
    xmlrpclib.dumps((float(xmlrpclib.MAXINT + 42), float(xmlrpclib.MININT - 42)))

    def dummy_write(s):
        pass
    m = xmlrpclib.Marshaller()
    m.dump_double(xmlrpclib.MAXINT, dummy_write)
    m.dump_double(xmlrpclib.MININT, dummy_write)
    m.dump_double(xmlrpclib.MAXINT + 42, dummy_write)
    m.dump_double(xmlrpclib.MININT - 42, dummy_write)
