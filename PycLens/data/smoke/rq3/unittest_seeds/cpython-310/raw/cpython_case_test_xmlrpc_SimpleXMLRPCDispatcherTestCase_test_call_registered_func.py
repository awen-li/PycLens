# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleXMLRPCDispatcherTestCase_test_call_registered_func

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exp_params = (1, 2, 3)

    def dispatched_func(*params):
        raise self.DispatchExc(params)
    dispatcher = xmlrpc.server.SimpleXMLRPCDispatcher()
    dispatcher.register_function(dispatched_func)
    with self.assertRaises(self.DispatchExc) as exc_ctx:
        dispatcher._dispatch('dispatched_func', exp_params)
    self.assertEqual(exc_ctx.exception.args, (exp_params,))
    self.assertIsNone(exc_ctx.exception.__cause__)
    self.assertIsNone(exc_ctx.exception.__context__)
