# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_await_7

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Awaitable:

        def __await__(self):
            yield 42
            return 100

    async def foo():
        return await Awaitable()
    self.assertEqual(run_async(foo()), ([42], 100))
