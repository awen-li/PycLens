# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenTest_test_async_gen_exception_03

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        await awaitable()
        yield 123
        await awaitable(throw=True)
        yield 456
    with self.assertRaises(AwaitException):
        to_list(gen())
