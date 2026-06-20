# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: DateTimeTestCase_test_time_struct

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = time.localtime(1181399930.036952)
    t = xmlrpclib.DateTime(d)
    self.assertEqual(str(t), time.strftime('%Y%m%dT%H:%M:%S', d))
