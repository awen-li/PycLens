# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_contextmanager_trap_yield_after_throw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @contextmanager
    def whoo():
        try:
            yield
        except:
            yield
    ctx = whoo()
    ctx.__enter__()
    self.assertRaises(RuntimeError, ctx.__exit__, TypeError, TypeError('foo'), None)
