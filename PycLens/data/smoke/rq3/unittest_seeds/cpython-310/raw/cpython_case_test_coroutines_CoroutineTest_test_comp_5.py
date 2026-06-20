# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_comp_5

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def f(it):
        for i in it:
            yield i

    async def run_list():
        return [i + 1 for pair in ([10, 20], [30, 40]) if pair[0] > 10 async for i in f(pair) if i > 30]
    self.assertEqual(run_async(run_list()), ([], [41]))
