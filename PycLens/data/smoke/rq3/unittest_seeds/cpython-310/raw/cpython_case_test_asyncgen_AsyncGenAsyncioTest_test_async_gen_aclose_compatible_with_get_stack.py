# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_aclose_compatible_with_get_stack

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def async_generator():
        yield object()

    async def run():
        ag = async_generator()
        asyncio.create_task(ag.aclose())
        tasks = asyncio.all_tasks()
        for task in tasks:
            task.get_stack()
    self.loop.run_until_complete(run())
