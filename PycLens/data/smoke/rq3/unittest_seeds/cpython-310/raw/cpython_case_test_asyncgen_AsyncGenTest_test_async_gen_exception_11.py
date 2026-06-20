# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenTest_test_async_gen_exception_11

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def sync_gen():
        yield 10
        yield 20

    def sync_gen_wrapper():
        yield 1
        sg = sync_gen()
        sg.send(None)
        try:
            sg.throw(GeneratorExit())
        except GeneratorExit:
            yield 2
        yield 3

    async def async_gen():
        yield 10
        yield 20

    async def async_gen_wrapper():
        yield 1
        asg = async_gen()
        await asg.asend(None)
        try:
            await asg.athrow(GeneratorExit())
        except GeneratorExit:
            yield 2
        yield 3
    self.compare_generators(sync_gen_wrapper(), async_gen_wrapper())
