# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_getset_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    v1 = contextvars.ContextVar('v1')
    v2 = contextvars.ContextVar('v2')
    t1 = v1.set(42)
    with self.assertRaisesRegex(ValueError, 'by a different'):
        v2.reset(t1)
