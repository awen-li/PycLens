# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def bar():
        return (yield from coro)

    async def foo():
        return 'spam'
    coro = foo()
    self.assertEqual(run_async(bar()), ([], 'spam'))
    coro.close()
