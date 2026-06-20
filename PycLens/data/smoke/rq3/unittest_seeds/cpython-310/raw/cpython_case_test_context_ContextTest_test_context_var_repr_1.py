# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_var_repr_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = contextvars.ContextVar('a')
    self.assertIn('a', repr(c))
    c = contextvars.ContextVar('a', default=123)
    self.assertIn('123', repr(c))
    lst = []
    c = contextvars.ContextVar('a', default=lst)
    lst.append(c)
    self.assertIn('...', repr(c))
    self.assertIn('...', repr(lst))
    t = c.set(1)
    self.assertIn(repr(c), repr(t))
    self.assertNotIn(' used ', repr(t))
    c.reset(t)
    self.assertIn(' used ', repr(t))
