# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_datetime_before_1900

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dt = datetime.datetime(1, 2, 10, 11, 41, 23)
    self.assertEqual(dt, xmlrpclib.DateTime('00010210T11:41:23'))
    s = xmlrpclib.dumps((dt,))
    (result, m) = xmlrpclib.loads(s, use_builtin_types=True)
    (newdt,) = result
    self.assertEqual(newdt, dt)
    self.assertIs(type(newdt), datetime.datetime)
    self.assertIsNone(m)
    (result, m) = xmlrpclib.loads(s, use_builtin_types=False)
    (newdt,) = result
    self.assertEqual(newdt, dt)
    self.assertIs(type(newdt), xmlrpclib.DateTime)
    self.assertIsNone(m)
