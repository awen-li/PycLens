# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def func():
        pass
    coro = func()
    with self.assertRaises(TypeError):
        copy.copy(coro)
    aw = coro.__await__()
    try:
        with self.assertRaises(TypeError):
            copy.copy(aw)
    finally:
        aw.close()
