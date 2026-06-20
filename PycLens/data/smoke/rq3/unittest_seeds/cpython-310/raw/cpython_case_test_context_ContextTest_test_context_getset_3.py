# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_getset_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = contextvars.ContextVar('c', default=42)
    ctx = contextvars.Context()

    def fun():
        self.assertEqual(c.get(), 42)
        with self.assertRaises(KeyError):
            ctx[c]
        self.assertIsNone(ctx.get(c))
        self.assertEqual(ctx.get(c, 'spam'), 'spam')
        self.assertNotIn(c, ctx)
        self.assertEqual(list(ctx.keys()), [])
        t = c.set(1)
        self.assertEqual(list(ctx.keys()), [c])
        self.assertEqual(ctx[c], 1)
        c.reset(t)
        self.assertEqual(list(ctx.keys()), [])
        with self.assertRaises(KeyError):
            ctx[c]
    ctx.run(fun)
