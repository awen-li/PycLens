# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_anext_bad_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        yield 1

    async def call_with_too_few_args():
        await anext()

    async def call_with_too_many_args():
        await anext(gen(), 1, 3)

    async def call_with_wrong_type_args():
        await anext(1, gen())

    async def call_with_kwarg():
        await anext(aiterator=gen())
    with self.assertRaises(TypeError):
        self.loop.run_until_complete(call_with_too_few_args())
    with self.assertRaises(TypeError):
        self.loop.run_until_complete(call_with_too_many_args())
    with self.assertRaises(TypeError):
        self.loop.run_until_complete(call_with_wrong_type_args())
    with self.assertRaises(TypeError):
        self.loop.run_until_complete(call_with_kwarg())
