# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_comp_4_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def f(it):
        for i in it:
            yield i

    async def run_list():
        return [i + 10 async for i in f(range(5)) if 0 < i < 4]
    self.assertEqual(run_async(run_list()), ([], [11, 12, 13]))

    async def run_set():
        return {i + 10 async for i in f(range(5)) if 0 < i < 4}
    self.assertEqual(run_async(run_set()), ([], {11, 12, 13}))

    async def run_dict():
        return {i + 10: i + 100 async for i in f(range(5)) if 0 < i < 4}
    self.assertEqual(run_async(run_dict()), ([], {11: 101, 12: 102, 13: 103}))

    async def run_gen():
        gen = (i + 10 async for i in f(range(5)) if 0 < i < 4)
        return [g + 100 async for g in gen]
    self.assertEqual(run_async(run_gen()), ([], [111, 112, 113]))
