# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_shutdown_01

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    finalized = 0

    async def waiter(timeout):
        nonlocal finalized
        try:
            await asyncio.sleep(timeout)
            yield 1
        finally:
            await asyncio.sleep(0)
            finalized += 1

    async def wait():
        async for _ in waiter(1):
            pass
    t1 = self.loop.create_task(wait())
    t2 = self.loop.create_task(wait())
    self.loop.run_until_complete(asyncio.sleep(0.1))
    t1.cancel()
    t2.cancel()
    with self.assertRaises(asyncio.CancelledError):
        self.loop.run_until_complete(t1)
    with self.assertRaises(asyncio.CancelledError):
        self.loop.run_until_complete(t2)
    self.loop.run_until_complete(self.loop.shutdown_asyncgens())
    self.assertEqual(finalized, 2)
