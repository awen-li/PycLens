# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_comp_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def f(i):
        return i

    async def run_list():
        return [s for c in [f(''), f('abc'), f(''), f(['de', 'fg'])] for s in await c]
    self.assertEqual(run_async(run_list()), ([], ['a', 'b', 'c', 'de', 'fg']))

    async def run_set():
        return {d for c in [f([f([10, 30]), f([20])])] for s in await c for d in await s}
    self.assertEqual(run_async(run_set()), ([], {10, 20, 30}))

    async def run_set2():
        return {await s for c in [f([f(10), f(20)])] for s in await c}
    self.assertEqual(run_async(run_set2()), ([], {10, 20}))
