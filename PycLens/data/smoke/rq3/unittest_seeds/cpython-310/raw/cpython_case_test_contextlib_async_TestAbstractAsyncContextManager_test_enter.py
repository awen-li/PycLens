# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: TestAbstractAsyncContextManager_test_enter

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class DefaultEnter(AbstractAsyncContextManager):

        async def __aexit__(self, *args):
            await super().__aexit__(*args)
    manager = DefaultEnter()
    self.assertIs(await manager.__aenter__(), manager)
    async with manager as context:
        self.assertIs(manager, context)
