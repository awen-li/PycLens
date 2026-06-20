# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_with_11

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    CNT = 0

    class CM:

        async def __aenter__(self):
            raise NotImplementedError

        async def __aexit__(self, *e):
            1 / 0

    async def foo():
        nonlocal CNT
        async with CM():
            raise RuntimeError
    try:
        run_async(foo())
    except NotImplementedError as exc:
        self.assertTrue(exc.__context__ is None)
    else:
        self.fail('exception from __aenter__ did not propagate')
