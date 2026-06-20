# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: DateTimeTestCase_test_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = ' 20070908T07:11:13  '
    t1 = xmlrpclib.DateTime()
    t1.decode(d)
    tref = xmlrpclib.DateTime(datetime.datetime(2007, 9, 8, 7, 11, 13))
    self.assertEqual(t1, tref)
    t2 = xmlrpclib._datetime(d)
    self.assertEqual(t2, tref)
