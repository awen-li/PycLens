# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_for_assign_raising_stop_async_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadTarget:

        def __setitem__(self, key, value):
            raise StopAsyncIteration(42)
    tgt = BadTarget()

    async def source():
        yield 10

    async def run_for():
        with self.assertRaises(StopAsyncIteration) as cm:
            async for tgt[0] in source():
                pass
        self.assertEqual(cm.exception.args, (42,))
        return 'end'
    self.assertEqual(run_async(run_for()), ([], 'end'))

    async def run_list():
        with self.assertRaises(StopAsyncIteration) as cm:
            return [0 async for tgt[0] in source()]
        self.assertEqual(cm.exception.args, (42,))
        return 'end'
    self.assertEqual(run_async(run_list()), ([], 'end'))

    async def run_gen():
        gen = (0 async for tgt[0] in source())
        a = gen.asend(None)
        with self.assertRaises(RuntimeError) as cm:
            await a
        self.assertIsInstance(cm.exception.__cause__, StopAsyncIteration)
        self.assertEqual(cm.exception.__cause__.args, (42,))
        return 'end'
    self.assertEqual(run_async(run_gen()), ([], 'end'))
