# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_19

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    CHK = 0

    @types.coroutine
    def foo():
        nonlocal CHK
        yield
        try:
            yield
        except GeneratorExit:
            CHK += 1

    async def coroutine():
        await foo()
    coro = coroutine()
    coro.send(None)
    coro.send(None)
    self.assertEqual(CHK, 0)
    coro.close()
    self.assertEqual(CHK, 1)
    for _ in range(3):
        coro.close()
        self.assertEqual(CHK, 1)
