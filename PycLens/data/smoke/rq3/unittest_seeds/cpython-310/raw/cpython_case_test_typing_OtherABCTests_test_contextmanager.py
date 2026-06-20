# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: OtherABCTests_test_contextmanager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @contextlib.contextmanager
    def manager():
        yield 42
    cm = manager()
    self.assertIsInstance(cm, typing.ContextManager)
    self.assertNotIsInstance(42, typing.ContextManager)
