# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        raise StopIteration
    with self.assertRaisesRegex(RuntimeError, 'coroutine raised StopIteration'):
        run_async(foo())
