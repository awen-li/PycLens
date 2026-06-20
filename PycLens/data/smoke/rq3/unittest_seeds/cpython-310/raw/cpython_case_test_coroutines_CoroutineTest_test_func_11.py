# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_11

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def func():
        pass
    coro = func()
    self.assertIn('__await__', dir(coro))
    self.assertIn('__iter__', dir(coro.__await__()))
    self.assertIn('coroutine_wrapper', repr(coro.__await__()))
    coro.close()
