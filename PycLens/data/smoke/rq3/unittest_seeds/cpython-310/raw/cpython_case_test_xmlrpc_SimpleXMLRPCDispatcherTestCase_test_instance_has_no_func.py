# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleXMLRPCDispatcherTestCase_test_instance_has_no_func

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dispatcher = xmlrpc.server.SimpleXMLRPCDispatcher()
    dispatcher.register_instance(object())
    with self.assertRaisesRegex(Exception, 'method'):
        dispatcher._dispatch('method', ('param',))
