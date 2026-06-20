# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenTest_test_async_gen_exception_09

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def sync_gen():
        try:
            yield 1
            1 / 0
        finally:
            yield 2
            yield 3
        yield 100

    async def async_gen():
        try:
            await awaitable()
            yield 1
            1 / 0
        finally:
            yield 2
            await awaitable()
            yield 3
        yield 100
    self.compare_generators(sync_gen(), async_gen())
