# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_with_5

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CM:

        async def __aenter__(self):
            return self

        async def __aexit__(self, *exc):
            pass

    async def func():
        async with CM():
            self.assertEqual((1,), 1)
    with self.assertRaises(AssertionError):
        run_async(func())
