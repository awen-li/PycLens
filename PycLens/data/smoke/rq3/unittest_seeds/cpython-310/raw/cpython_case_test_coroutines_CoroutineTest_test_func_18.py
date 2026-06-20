# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_18

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def coroutine():
        return 'spam'
    coro = coroutine()
    await_iter = coro.__await__()
    it = iter(await_iter)
    with self.assertRaisesRegex(StopIteration, 'spam'):
        it.send(None)
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        it.send(None)
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        next(it)
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        it.throw(Exception('wat'))
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        it.throw(Exception('wat'))
    it.close()
    it.close()
