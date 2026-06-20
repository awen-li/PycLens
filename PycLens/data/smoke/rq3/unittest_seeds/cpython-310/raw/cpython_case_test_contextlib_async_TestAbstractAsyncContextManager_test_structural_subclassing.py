# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: TestAbstractAsyncContextManager_test_structural_subclassing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ManagerFromScratch:

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc_value, traceback):
            return None
    self.assertTrue(issubclass(ManagerFromScratch, AbstractAsyncContextManager))

    class DefaultEnter(AbstractAsyncContextManager):

        async def __aexit__(self, *args):
            await super().__aexit__(*args)
    self.assertTrue(issubclass(DefaultEnter, AbstractAsyncContextManager))

    class NoneAenter(ManagerFromScratch):
        __aenter__ = None
    self.assertFalse(issubclass(NoneAenter, AbstractAsyncContextManager))

    class NoneAexit(ManagerFromScratch):
        __aexit__ = None
    self.assertFalse(issubclass(NoneAexit, AbstractAsyncContextManager))
