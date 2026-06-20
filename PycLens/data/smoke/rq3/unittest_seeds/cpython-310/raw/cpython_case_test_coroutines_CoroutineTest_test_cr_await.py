# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_cr_await

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def a():
        self.assertEqual(inspect.getcoroutinestate(coro_b), inspect.CORO_RUNNING)
        self.assertIsNone(coro_b.cr_await)
        yield
        self.assertEqual(inspect.getcoroutinestate(coro_b), inspect.CORO_RUNNING)
        self.assertIsNone(coro_b.cr_await)

    async def c():
        await a()

    async def b():
        self.assertIsNone(coro_b.cr_await)
        await c()
        self.assertIsNone(coro_b.cr_await)
    coro_b = b()
    self.assertEqual(inspect.getcoroutinestate(coro_b), inspect.CORO_CREATED)
    self.assertIsNone(coro_b.cr_await)
    coro_b.send(None)
    self.assertEqual(inspect.getcoroutinestate(coro_b), inspect.CORO_SUSPENDED)
    self.assertEqual(coro_b.cr_await.cr_await.gi_code.co_name, 'a')
    with self.assertRaises(StopIteration):
        coro_b.send(None)
    self.assertEqual(inspect.getcoroutinestate(coro_b), inspect.CORO_CLOSED)
    self.assertIsNone(coro_b.cr_await)
