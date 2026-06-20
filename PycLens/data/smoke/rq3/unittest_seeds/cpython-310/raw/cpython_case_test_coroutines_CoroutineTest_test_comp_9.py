# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_comp_9

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        yield 1
        yield 2

    async def f():
        l = [i async for i in gen()]
        return [i for i in l]
    self.assertEqual(run_async(f()), ([], [1, 2]))
