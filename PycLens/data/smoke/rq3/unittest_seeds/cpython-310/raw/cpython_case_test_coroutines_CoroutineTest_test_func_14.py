# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_14

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def gen():
        yield

    async def coro():
        try:
            await gen()
        except GeneratorExit:
            await gen()
    c = coro()
    c.send(None)
    with self.assertRaisesRegex(RuntimeError, 'coroutine ignored GeneratorExit'):
        c.close()
