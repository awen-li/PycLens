# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: DateTimeTestCase_test_time_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = (2007, 6, 9, 10, 38, 50, 5, 160, 0)
    t = xmlrpclib.DateTime(d)
    self.assertEqual(str(t), '20070609T10:38:50')
