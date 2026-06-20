# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: TestType_test_new_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = type('A', (), {})
    self.assertEqual(A.__name__, 'A')
    self.assertEqual(A.__qualname__, 'A')
    self.assertEqual(A.__module__, __name__)
    self.assertEqual(A.__bases__, (object,))
    self.assertIs(A.__base__, object)
    x = A()
    self.assertIs(type(x), A)
    self.assertIs(x.__class__, A)

    class B:

        def ham(self):
            return 'ham%d' % self
    C = type('C', (B, int), {'spam': lambda self: 'spam%s' % self})
    self.assertEqual(C.__name__, 'C')
    self.assertEqual(C.__qualname__, 'C')
    self.assertEqual(C.__module__, __name__)
    self.assertEqual(C.__bases__, (B, int))
    self.assertIs(C.__base__, int)
    self.assertIn('spam', C.__dict__)
    self.assertNotIn('ham', C.__dict__)
    x = C(42)
    self.assertEqual(x, 42)
    self.assertIs(type(x), C)
    self.assertIs(x.__class__, C)
    self.assertEqual(x.ham(), 'ham42')
    self.assertEqual(x.spam(), 'spam42')
    self.assertEqual(x.to_bytes(2, 'little'), b'*\x00')
