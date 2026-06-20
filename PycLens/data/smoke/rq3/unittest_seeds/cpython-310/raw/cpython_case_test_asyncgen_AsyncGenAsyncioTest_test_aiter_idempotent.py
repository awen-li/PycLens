# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_aiter_idempotent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        yield 1
    applied_once = aiter(gen())
    applied_twice = aiter(applied_once)
    self.assertIs(applied_once, applied_twice)
