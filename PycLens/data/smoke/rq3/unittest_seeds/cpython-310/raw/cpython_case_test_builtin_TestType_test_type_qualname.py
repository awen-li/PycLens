# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestType_test_type_qualname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = type('A', (), {'__qualname__': 'B.C'})
    self.assertEqual(A.__name__, 'A')
    self.assertEqual(A.__qualname__, 'B.C')
    self.assertEqual(A.__module__, __name__)
    with self.assertRaises(TypeError):
        type('A', (), {'__qualname__': b'B'})
    self.assertEqual(A.__qualname__, 'B.C')
    A.__qualname__ = 'D.E'
    self.assertEqual(A.__name__, 'A')
    self.assertEqual(A.__qualname__, 'D.E')
    with self.assertRaises(TypeError):
        A.__qualname__ = b'B'
    self.assertEqual(A.__qualname__, 'D.E')
