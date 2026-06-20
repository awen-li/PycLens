# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_with_4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CM:
        pass
    body_executed = None

    async def foo():
        nonlocal body_executed
        body_executed = False
        async with CM():
            body_executed = True
    with self.assertRaisesRegex(AttributeError, '__aenter__'):
        run_async(foo())
    self.assertIs(body_executed, False)
