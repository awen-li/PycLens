# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_run_5

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = contextvars.Context()
    var = contextvars.ContextVar('var')

    def func():
        self.assertIsNone(var.get(None))
        var.set('spam')
        1 / 0
    with self.assertRaises(ZeroDivisionError):
        ctx.run(func)
    self.assertIsNone(var.get(None))
