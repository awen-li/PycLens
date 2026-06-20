# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_getset_5

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = contextvars.ContextVar('c', default=42)
    c.set([])

    def fun():
        c.set([])
        c.get().append(42)
        self.assertEqual(c.get(), [42])
    contextvars.copy_context().run(fun)
    self.assertEqual(c.get(), [])
