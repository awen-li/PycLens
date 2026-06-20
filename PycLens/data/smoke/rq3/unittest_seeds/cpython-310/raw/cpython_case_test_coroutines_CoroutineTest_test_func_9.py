# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_9

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        pass
    with self.assertWarnsRegex(RuntimeWarning, "coroutine '.*test_func_9.*foo' was never awaited"):
        foo()
        support.gc_collect()
    with self.assertWarnsRegex(RuntimeWarning, "coroutine '.*test_func_9.*foo' was never awaited"):
        with self.assertRaises(TypeError):
            for _ in foo():
                pass
        support.gc_collect()
