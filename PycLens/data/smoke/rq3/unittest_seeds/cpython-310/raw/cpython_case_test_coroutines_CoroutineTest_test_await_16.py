# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_await_16

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def f():
        return ValueError()

    async def g():
        try:
            raise KeyError
        except:
            return await f()
    (_, result) = run_async(g())
    self.assertIsNone(result.__context__)
