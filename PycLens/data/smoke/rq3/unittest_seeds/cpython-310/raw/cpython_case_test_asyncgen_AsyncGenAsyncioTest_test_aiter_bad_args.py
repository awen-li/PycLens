# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_aiter_bad_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        yield 1

    async def call_with_too_few_args():
        await aiter()

    async def call_with_too_many_args():
        await aiter(gen(), 1)

    async def call_with_wrong_type_arg():
        await aiter(1)
    with self.assertRaises(TypeError):
        self.loop.run_until_complete(call_with_too_few_args())
    with self.assertRaises(TypeError):
        self.loop.run_until_complete(call_with_too_many_args())
    with self.assertRaises(TypeError):
        self.loop.run_until_complete(call_with_wrong_type_arg())
