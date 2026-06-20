# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleXMLRPCDispatcherTestCase_test_call_dispatch_func

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exp_method = 'method'
    exp_params = (1, 2, 3)

    class TestInstance:

        def _dispatch(self, method, params):
            raise SimpleXMLRPCDispatcherTestCase.DispatchExc(method, params)
    dispatcher = xmlrpc.server.SimpleXMLRPCDispatcher()
    dispatcher.register_instance(TestInstance())
    with self.assertRaises(self.DispatchExc) as exc_ctx:
        dispatcher._dispatch(exp_method, exp_params)
    self.assertEqual(exc_ctx.exception.args, (exp_method, exp_params))
    self.assertIsNone(exc_ctx.exception.__cause__)
    self.assertIsNone(exc_ctx.exception.__context__)
