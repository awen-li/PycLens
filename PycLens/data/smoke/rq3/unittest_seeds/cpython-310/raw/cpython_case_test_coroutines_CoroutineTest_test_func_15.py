# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_15

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def spammer():
        return 'spam'

    async def reader(coro):
        return await coro
    spammer_coro = spammer()
    with self.assertRaisesRegex(StopIteration, 'spam'):
        reader(spammer_coro).send(None)
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        reader(spammer_coro).send(None)
