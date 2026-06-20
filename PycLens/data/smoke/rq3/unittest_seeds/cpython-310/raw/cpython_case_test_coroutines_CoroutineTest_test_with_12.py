# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_with_12

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    CNT = 0

    class CM:

        async def __aenter__(self):
            return self

        async def __aexit__(self, *e):
            return True

    async def foo():
        nonlocal CNT
        async with CM() as cm:
            self.assertIs(cm.__class__, CM)
            raise RuntimeError
    run_async(foo())
