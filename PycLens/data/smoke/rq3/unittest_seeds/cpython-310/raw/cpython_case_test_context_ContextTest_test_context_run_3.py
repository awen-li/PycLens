# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_run_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = contextvars.Context()

    def func(*args, **kwargs):
        1 / 0
    with self.assertRaises(ZeroDivisionError):
        ctx.run(func)
    with self.assertRaises(ZeroDivisionError):
        ctx.run(func, 1, 2)
    with self.assertRaises(ZeroDivisionError):
        ctx.run(func, 1, 2, a=123)
