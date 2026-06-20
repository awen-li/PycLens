# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestType_test_type_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in ('A', 'Ä', '🐍', 'B.A', '42', ''):
        with self.subTest(name=name):
            A = type(name, (), {})
            self.assertEqual(A.__name__, name)
            self.assertEqual(A.__qualname__, name)
            self.assertEqual(A.__module__, __name__)
    with self.assertRaises(ValueError):
        type('A\x00B', (), {})
    with self.assertRaises(UnicodeEncodeError):
        type('A\udcdcB', (), {})
    with self.assertRaises(TypeError):
        type(b'A', (), {})
    C = type('C', (), {})
    for name in ('A', 'Ä', '🐍', 'B.A', '42', ''):
        with self.subTest(name=name):
            C.__name__ = name
            self.assertEqual(C.__name__, name)
            self.assertEqual(C.__qualname__, 'C')
            self.assertEqual(C.__module__, __name__)
    A = type('C', (), {})
    with self.assertRaises(ValueError):
        A.__name__ = 'A\x00B'
    self.assertEqual(A.__name__, 'C')
    with self.assertRaises(UnicodeEncodeError):
        A.__name__ = 'A\udcdcB'
    self.assertEqual(A.__name__, 'C')
    with self.assertRaises(TypeError):
        A.__name__ = b'A'
    self.assertEqual(A.__name__, 'C')
