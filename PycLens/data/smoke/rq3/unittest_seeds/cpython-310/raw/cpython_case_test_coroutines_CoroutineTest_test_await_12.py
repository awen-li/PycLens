# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_await_12

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def coro():
        return 'spam'
    c = coro()

    class Awaitable:

        def __await__(self):
            return c

    async def foo():
        return await Awaitable()
    with self.assertRaisesRegex(TypeError, '__await__\\(\\) returned a coroutine'):
        run_async(foo())
    c.close()
