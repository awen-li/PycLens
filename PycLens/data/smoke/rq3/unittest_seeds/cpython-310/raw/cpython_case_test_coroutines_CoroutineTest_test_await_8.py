# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_await_8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Awaitable:
        pass

    async def foo():
        return await Awaitable()
    with self.assertRaisesRegex(TypeError, "object Awaitable can't be used in 'await' expression"):
        run_async(foo())
