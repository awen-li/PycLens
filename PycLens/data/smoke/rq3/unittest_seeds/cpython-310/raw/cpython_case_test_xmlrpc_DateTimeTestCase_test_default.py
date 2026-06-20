# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: DateTimeTestCase_test_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with mock.patch('time.localtime') as localtime_mock:
        time_struct = time.struct_time([2013, 7, 15, 0, 24, 49, 0, 196, 0])
        localtime_mock.return_value = time_struct
        localtime = time.localtime()
        t = xmlrpclib.DateTime()
        self.assertEqual(str(t), time.strftime('%Y%m%dT%H:%M:%S', localtime))
