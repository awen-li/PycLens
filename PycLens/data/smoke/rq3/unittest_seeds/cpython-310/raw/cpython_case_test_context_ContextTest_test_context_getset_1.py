# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_getset_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = contextvars.ContextVar('c')
    with self.assertRaises(LookupError):
        c.get()
    self.assertIsNone(c.get(None))
    t0 = c.set(42)
    self.assertEqual(c.get(), 42)
    self.assertEqual(c.get(None), 42)
    self.assertIs(t0.old_value, t0.MISSING)
    self.assertIs(t0.old_value, contextvars.Token.MISSING)
    self.assertIs(t0.var, c)
    t = c.set('spam')
    self.assertEqual(c.get(), 'spam')
    self.assertEqual(c.get(None), 'spam')
    self.assertEqual(t.old_value, 42)
    c.reset(t)
    self.assertEqual(c.get(), 42)
    self.assertEqual(c.get(None), 42)
    c.set('spam2')
    with self.assertRaisesRegex(RuntimeError, 'has already been used'):
        c.reset(t)
    self.assertEqual(c.get(), 'spam2')
    ctx1 = contextvars.copy_context()
    self.assertIn(c, ctx1)
    c.reset(t0)
    with self.assertRaisesRegex(RuntimeError, 'has already been used'):
        c.reset(t0)
    self.assertIsNone(c.get(None))
    self.assertIn(c, ctx1)
    self.assertEqual(ctx1[c], 'spam2')
    self.assertEqual(ctx1.get(c, 'aa'), 'spam2')
    self.assertEqual(len(ctx1), 1)
    self.assertEqual(list(ctx1.items()), [(c, 'spam2')])
    self.assertEqual(list(ctx1.values()), ['spam2'])
    self.assertEqual(list(ctx1.keys()), [c])
    self.assertEqual(list(ctx1), [c])
    ctx2 = contextvars.copy_context()
    self.assertNotIn(c, ctx2)
    with self.assertRaises(KeyError):
        ctx2[c]
    self.assertEqual(ctx2.get(c, 'aa'), 'aa')
    self.assertEqual(len(ctx2), 0)
    self.assertEqual(list(ctx2), [])
