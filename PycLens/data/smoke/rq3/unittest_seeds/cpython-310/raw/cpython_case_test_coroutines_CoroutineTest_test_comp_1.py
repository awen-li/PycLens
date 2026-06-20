# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_comp_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def f(i):
        return i

    async def run_list():
        return [await c for c in [f(1), f(41)]]

    async def run_set():
        return {await c for c in [f(1), f(41)]}

    async def run_dict1():
        return {await c: 'a' for c in [f(1), f(41)]}

    async def run_dict2():
        return {i: await c for (i, c) in enumerate([f(1), f(41)])}
    self.assertEqual(run_async(run_list()), ([], [1, 41]))
    self.assertEqual(run_async(run_set()), ([], {1, 41}))
    self.assertEqual(run_async(run_dict1()), ([], {1: 'a', 41: 'a'}))
    self.assertEqual(run_async(run_dict2()), ([], {0: 1, 1: 41}))
