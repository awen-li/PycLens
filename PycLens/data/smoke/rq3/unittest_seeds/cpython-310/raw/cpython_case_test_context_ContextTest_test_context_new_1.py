# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_new_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'any arguments'):
        contextvars.Context(1)
    with self.assertRaisesRegex(TypeError, 'any arguments'):
        contextvars.Context(1, a=1)
    with self.assertRaisesRegex(TypeError, 'any arguments'):
        contextvars.Context(a=1)
    contextvars.Context(**{})
