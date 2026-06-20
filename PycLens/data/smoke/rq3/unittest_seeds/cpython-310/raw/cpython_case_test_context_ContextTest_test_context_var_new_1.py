# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_context.py
# case: ContextTest_test_context_var_new_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'takes exactly 1'):
        contextvars.ContextVar()
    with self.assertRaisesRegex(TypeError, 'must be a str'):
        contextvars.ContextVar(1)
    c = contextvars.ContextVar('aaa')
    self.assertEqual(c.name, 'aaa')
    with self.assertRaises(AttributeError):
        c.name = 'bbb'
    self.assertNotEqual(hash(c), hash('aaa'))
