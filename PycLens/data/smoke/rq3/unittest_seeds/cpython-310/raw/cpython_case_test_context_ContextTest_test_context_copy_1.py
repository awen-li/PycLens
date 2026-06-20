# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_copy_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx1 = contextvars.Context()
    c = contextvars.ContextVar('c', default=42)

    def ctx1_fun():
        c.set(10)
        ctx2 = ctx1.copy()
        self.assertEqual(ctx2[c], 10)
        c.set(20)
        self.assertEqual(ctx1[c], 20)
        self.assertEqual(ctx2[c], 10)
        ctx2.run(ctx2_fun)
        self.assertEqual(ctx1[c], 20)
        self.assertEqual(ctx2[c], 30)

    def ctx2_fun():
        self.assertEqual(c.get(), 10)
        c.set(30)
        self.assertEqual(c.get(), 30)
    ctx1.run(ctx1_fun)
