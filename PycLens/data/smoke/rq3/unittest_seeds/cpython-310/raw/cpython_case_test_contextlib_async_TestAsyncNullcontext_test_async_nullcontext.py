# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: TestAsyncNullcontext_test_async_nullcontext

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        pass
    c = C()
    async with nullcontext(c) as c_in:
        self.assertIs(c_in, c)
