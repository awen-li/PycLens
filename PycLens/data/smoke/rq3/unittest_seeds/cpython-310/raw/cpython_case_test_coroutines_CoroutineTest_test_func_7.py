# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_7

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def bar():
        return 10
    coro = bar()

    def foo():
        yield from coro
    with self.assertRaisesRegex(TypeError, "cannot 'yield from' a coroutine object in a non-coroutine generator"):
        list(foo())
    coro.close()
