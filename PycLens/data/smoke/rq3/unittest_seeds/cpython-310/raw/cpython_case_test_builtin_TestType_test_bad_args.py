# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestType_test_bad_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        type()
    with self.assertRaises(TypeError):
        type('A', ())
    with self.assertRaises(TypeError):
        type('A', (), {}, ())
    with self.assertRaises(TypeError):
        type('A', (), dict={})
    with self.assertRaises(TypeError):
        type('A', [], {})
    with self.assertRaises(TypeError):
        type('A', (), types.MappingProxyType({}))
    with self.assertRaises(TypeError):
        type('A', (None,), {})
    with self.assertRaises(TypeError):
        type('A', (bool,), {})
    with self.assertRaises(TypeError):
        type('A', (int, str), {})
