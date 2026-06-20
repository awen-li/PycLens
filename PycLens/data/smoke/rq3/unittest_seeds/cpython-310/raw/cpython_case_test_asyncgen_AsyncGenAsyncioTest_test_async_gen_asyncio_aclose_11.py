# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_aclose_11

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DONE = 0

    def foo():
        try:
            yield
        except:
            pass
        yield
    g = foo()
    g.send(None)
    with self.assertRaisesRegex(RuntimeError, 'ignored GeneratorExit'):
        g.close()

    async def gen():
        nonlocal DONE
        try:
            yield
        except:
            pass
        yield
        DONE += 1

    async def run():
        nonlocal DONE
        g = gen()
        await g.asend(None)
        with self.assertRaisesRegex(RuntimeError, 'ignored GeneratorExit'):
            await g.aclose()
        DONE += 10
    self.loop.run_until_complete(run())
    self.assertEqual(DONE, 10)
