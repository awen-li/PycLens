# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestType_test_bad_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        type('A', (), {'__slots__': b'x'})
    with self.assertRaises(TypeError):
        type('A', (int,), {'__slots__': 'x'})
    with self.assertRaises(TypeError):
        type('A', (), {'__slots__': ''})
    with self.assertRaises(TypeError):
        type('A', (), {'__slots__': '42'})
    with self.assertRaises(TypeError):
        type('A', (), {'__slots__': 'x\x00y'})
    with self.assertRaises(ValueError):
        type('A', (), {'__slots__': 'x', 'x': 0})
    with self.assertRaises(TypeError):
        type('A', (), {'__slots__': ('__dict__', '__dict__')})
    with self.assertRaises(TypeError):
        type('A', (), {'__slots__': ('__weakref__', '__weakref__')})

    class B:
        pass
    with self.assertRaises(TypeError):
        type('A', (B,), {'__slots__': '__dict__'})
    with self.assertRaises(TypeError):
        type('A', (B,), {'__slots__': '__weakref__'})
