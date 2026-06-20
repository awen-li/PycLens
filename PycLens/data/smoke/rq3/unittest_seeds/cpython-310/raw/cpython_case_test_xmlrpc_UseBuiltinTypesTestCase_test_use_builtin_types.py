# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: UseBuiltinTypesTestCase_test_use_builtin_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.log = []
    expected_bytes = b'my dog has fleas'
    expected_date = datetime.datetime(2008, 5, 26, 18, 25, 12)
    marshaled = xmlrpclib.dumps((expected_bytes, expected_date), 'foobar')

    def foobar(*args):
        self.log.extend(args)
    handler = xmlrpc.server.SimpleXMLRPCDispatcher(allow_none=True, encoding=None, use_builtin_types=True)
    handler.register_function(foobar)
    handler._marshaled_dispatch(marshaled)
    self.assertEqual(len(self.log), 2)
    (mybytes, mydate) = self.log
    self.assertEqual(self.log, [expected_bytes, expected_date])
    self.assertIs(type(mydate), datetime.datetime)
    self.assertIs(type(mybytes), bytes)
