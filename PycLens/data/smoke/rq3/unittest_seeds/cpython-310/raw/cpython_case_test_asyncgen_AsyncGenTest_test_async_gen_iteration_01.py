# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenTest_test_async_gen_iteration_01

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        await awaitable()
        a = (yield 123)
        self.assertIs(a, None)
        await awaitable()
        yield 456
        await awaitable()
        yield 789
    self.assertEqual(to_list(gen()), [123, 456, 789])
