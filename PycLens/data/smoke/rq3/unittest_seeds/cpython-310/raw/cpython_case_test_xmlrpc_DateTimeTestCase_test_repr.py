# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: DateTimeTestCase_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = datetime.datetime(2007, 1, 2, 3, 4, 5)
    t = xmlrpclib.DateTime(d)
    val = "<DateTime '20070102T03:04:05' at %#x>" % id(t)
    self.assertEqual(repr(t), val)
