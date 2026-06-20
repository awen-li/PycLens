# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_run_7

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = contextvars.Context()

    def fun():
        with self.assertRaisesRegex(RuntimeError, 'is already entered'):
            ctx.run(fun)
    ctx.run(fun)
