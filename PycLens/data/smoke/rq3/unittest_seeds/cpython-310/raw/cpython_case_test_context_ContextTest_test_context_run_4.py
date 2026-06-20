# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_run_4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx1 = contextvars.Context()
    ctx2 = contextvars.Context()
    var = contextvars.ContextVar('var')

    def func2():
        self.assertIsNone(var.get(None))

    def func1():
        self.assertIsNone(var.get(None))
        var.set('spam')
        ctx2.run(func2)
        self.assertEqual(var.get(None), 'spam')
        cur = contextvars.copy_context()
        self.assertEqual(len(cur), 1)
        self.assertEqual(cur[var], 'spam')
        return cur
    returned_ctx = ctx1.run(func1)
    self.assertEqual(ctx1, returned_ctx)
    self.assertEqual(returned_ctx[var], 'spam')
    self.assertIn(var, returned_ctx)
