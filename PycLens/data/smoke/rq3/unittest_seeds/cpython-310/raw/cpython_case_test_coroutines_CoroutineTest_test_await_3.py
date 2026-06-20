# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_await_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        await AsyncYieldFrom([1, 2, 3])
    self.assertEqual(run_async(foo()), ([1, 2, 3], None))
    self.assertEqual(run_async__await__(foo()), ([1, 2, 3], None))
