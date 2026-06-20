# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_16

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def nop():
        yield

    async def send():
        await nop()
        return 'spam'

    async def read(coro):
        await nop()
        return await coro
    spammer = send()
    reader = read(spammer)
    reader.send(None)
    reader.send(None)
    with self.assertRaisesRegex(Exception, 'ham'):
        reader.throw(Exception('ham'))
    reader = read(spammer)
    reader.send(None)
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        reader.send(None)
    with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        reader.throw(Exception('wat'))
