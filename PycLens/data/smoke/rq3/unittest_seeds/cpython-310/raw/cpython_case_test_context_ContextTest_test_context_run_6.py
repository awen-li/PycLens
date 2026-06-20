# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_run_6

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = contextvars.Context()
    c = contextvars.ContextVar('a', default=0)

    def fun():
        self.assertEqual(c.get(), 0)
        self.assertIsNone(ctx.get(c))
        c.set(42)
        self.assertEqual(c.get(), 42)
        self.assertEqual(ctx.get(c), 42)
    ctx.run(fun)
