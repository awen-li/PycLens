# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_contextmanager_no_reraise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @contextmanager
    def whee():
        yield
    ctx = whee()
    ctx.__enter__()
    self.assertFalse(ctx.__exit__(TypeError, TypeError('foo'), None))
