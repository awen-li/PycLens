# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestBuggyCases_test_nested_class_definition_inside_async_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import asyncio
    self.addCleanup(asyncio.set_event_loop_policy, None)
    self.assertSourceEqual(asyncio.run(mod2.func225()), 226, 227)
    self.assertSourceEqual(mod2.cls226, 231, 235)
    self.assertSourceEqual(asyncio.run(mod2.cls226().func232()), 233, 234)
