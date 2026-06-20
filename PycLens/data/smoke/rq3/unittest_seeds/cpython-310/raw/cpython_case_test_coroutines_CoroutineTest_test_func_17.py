# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_17

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def coroutine():
        return 'spam'
    coro = coroutine()
    with self.assertRaisesRegex(StopIteration, 'spam'):
        coro.send(None)
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        coro.send(None)
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        coro.throw(Exception('wat'))
    coro.close()
    coro.close()
