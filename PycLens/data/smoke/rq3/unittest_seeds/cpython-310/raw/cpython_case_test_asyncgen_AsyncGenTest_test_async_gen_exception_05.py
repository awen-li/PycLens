# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenTest_test_async_gen_exception_05

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        yield 123
        raise StopAsyncIteration
    with self.assertRaisesRegex(RuntimeError, 'async generator.*StopAsyncIteration'):
        to_list(gen())
