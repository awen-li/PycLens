# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestAbstractContextManager_test_structural_subclassing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ManagerFromScratch:

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return None
    self.assertTrue(issubclass(ManagerFromScratch, AbstractContextManager))

    class DefaultEnter(AbstractContextManager):

        def __exit__(self, *args):
            super().__exit__(*args)
    self.assertTrue(issubclass(DefaultEnter, AbstractContextManager))

    class NoEnter(ManagerFromScratch):
        __enter__ = None
    self.assertFalse(issubclass(NoEnter, AbstractContextManager))

    class NoExit(ManagerFromScratch):
        __exit__ = None
    self.assertFalse(issubclass(NoExit, AbstractContextManager))
