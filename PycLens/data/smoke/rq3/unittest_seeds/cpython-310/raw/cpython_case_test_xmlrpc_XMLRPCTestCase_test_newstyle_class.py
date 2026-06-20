# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_newstyle_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class T(object):
        pass
    t = T()
    t.x = 100
    t.y = 'Hello'
    ((t2,), dummy) = xmlrpclib.loads(xmlrpclib.dumps((t,)))
    self.assertEqual(t2, t.__dict__)
