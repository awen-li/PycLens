# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_comp_10

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def f():
        xx = {i for i in [1, 2, 3]}
        return {x: x for x in xx}
    self.assertEqual(run_async(f()), ([], {1: 1, 2: 2, 3: 3}))
