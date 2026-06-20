# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_aiter_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    results = []

    class Gen:

        async def __aiter__(self):
            yield 1
            yield 2
    g = Gen()

    async def consume():
        ait = aiter(g)
        while True:
            try:
                results.append(await anext(ait))
            except StopAsyncIteration:
                break
    self.loop.run_until_complete(consume())
    self.assertEqual(results, [1, 2])
