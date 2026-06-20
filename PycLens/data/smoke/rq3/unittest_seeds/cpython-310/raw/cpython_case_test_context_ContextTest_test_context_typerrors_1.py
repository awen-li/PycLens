# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_typerrors_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = contextvars.Context()
    with self.assertRaisesRegex(TypeError, 'ContextVar key was expected'):
        ctx[1]
    with self.assertRaisesRegex(TypeError, 'ContextVar key was expected'):
        1 in ctx
    with self.assertRaisesRegex(TypeError, 'ContextVar key was expected'):
        ctx.get(1)
