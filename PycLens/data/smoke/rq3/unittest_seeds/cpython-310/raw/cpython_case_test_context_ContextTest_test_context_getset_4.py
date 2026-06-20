# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_getset_4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = contextvars.ContextVar('c', default=42)
    ctx = contextvars.Context()
    tok = ctx.run(c.set, 1)
    with self.assertRaisesRegex(ValueError, 'different Context'):
        c.reset(tok)
