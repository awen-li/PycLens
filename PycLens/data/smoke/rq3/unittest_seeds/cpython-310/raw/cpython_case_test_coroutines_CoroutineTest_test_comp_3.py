# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_comp_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def f(it):
        for i in it:
            yield i

    async def run_list():
        return [i + 1 async for i in f([10, 20])]
    self.assertEqual(run_async(run_list()), ([], [11, 21]))

    async def run_set():
        return {i + 1 async for i in f([10, 20])}
    self.assertEqual(run_async(run_set()), ([], {11, 21}))

    async def run_dict():
        return {i + 1: i + 2 async for i in f([10, 20])}
    self.assertEqual(run_async(run_dict()), ([], {11: 12, 21: 22}))

    async def run_gen():
        gen = (i + 1 async for i in f([10, 20]))
        return [g + 100 async for g in gen]
    self.assertEqual(run_async(run_gen()), ([], [111, 121]))
