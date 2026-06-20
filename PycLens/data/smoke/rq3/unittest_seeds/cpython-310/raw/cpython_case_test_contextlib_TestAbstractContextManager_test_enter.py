# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: TestAbstractContextManager_test_enter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class DefaultEnter(AbstractContextManager):

        def __exit__(self, *args):
            super().__exit__(*args)
    manager = DefaultEnter()
    self.assertIs(manager.__enter__(), manager)
