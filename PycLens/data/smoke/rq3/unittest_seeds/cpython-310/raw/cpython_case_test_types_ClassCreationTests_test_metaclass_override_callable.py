# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_metaclass_override_callable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    new_calls = []
    prepare_calls = []

    class ANotMeta:

        def __new__(mcls, *args, **kwargs):
            new_calls.append('ANotMeta')
            return super().__new__(mcls)

        @classmethod
        def __prepare__(mcls, name, bases):
            prepare_calls.append('ANotMeta')
            return {}

    class BNotMeta(ANotMeta):

        def __new__(mcls, *args, **kwargs):
            new_calls.append('BNotMeta')
            return super().__new__(mcls)

        @classmethod
        def __prepare__(mcls, name, bases):
            prepare_calls.append('BNotMeta')
            return super().__prepare__(name, bases)
    A = types.new_class('A', (), {'metaclass': ANotMeta})
    self.assertIs(ANotMeta, type(A))
    self.assertEqual(prepare_calls, ['ANotMeta'])
    prepare_calls.clear()
    self.assertEqual(new_calls, ['ANotMeta'])
    new_calls.clear()
    B = types.new_class('B', (), {'metaclass': BNotMeta})
    self.assertIs(BNotMeta, type(B))
    self.assertEqual(prepare_calls, ['BNotMeta', 'ANotMeta'])
    prepare_calls.clear()
    self.assertEqual(new_calls, ['BNotMeta', 'ANotMeta'])
    new_calls.clear()
    C = types.new_class('C', (A, B))
    self.assertIs(BNotMeta, type(C))
    self.assertEqual(prepare_calls, ['BNotMeta', 'ANotMeta'])
    prepare_calls.clear()
    self.assertEqual(new_calls, ['BNotMeta', 'ANotMeta'])
    new_calls.clear()
    C2 = types.new_class('C2', (B, A))
    self.assertIs(BNotMeta, type(C2))
    self.assertEqual(prepare_calls, ['BNotMeta', 'ANotMeta'])
    prepare_calls.clear()
    self.assertEqual(new_calls, ['BNotMeta', 'ANotMeta'])
    new_calls.clear()
    with self.assertRaises(TypeError):
        D = types.new_class('D', (C,), {'metaclass': type})
    E = types.new_class('E', (C,), {'metaclass': ANotMeta})
    self.assertIs(BNotMeta, type(E))
    self.assertEqual(prepare_calls, ['BNotMeta', 'ANotMeta'])
    prepare_calls.clear()
    self.assertEqual(new_calls, ['BNotMeta', 'ANotMeta'])
    new_calls.clear()
    F = types.new_class('F', (object(), C))
    self.assertIs(BNotMeta, type(F))
    self.assertEqual(prepare_calls, ['BNotMeta', 'ANotMeta'])
    prepare_calls.clear()
    self.assertEqual(new_calls, ['BNotMeta', 'ANotMeta'])
    new_calls.clear()
    F2 = types.new_class('F2', (C, object()))
    self.assertIs(BNotMeta, type(F2))
    self.assertEqual(prepare_calls, ['BNotMeta', 'ANotMeta'])
    prepare_calls.clear()
    self.assertEqual(new_calls, ['BNotMeta', 'ANotMeta'])
    new_calls.clear()
    with self.assertRaises(TypeError):
        X = types.new_class('X', (C, int()))
    with self.assertRaises(TypeError):
        X = types.new_class('X', (int(), C))
