# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_metaclass_derivation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    new_calls = []

    class AMeta(type):

        def __new__(mcls, name, bases, ns):
            new_calls.append('AMeta')
            return super().__new__(mcls, name, bases, ns)

        @classmethod
        def __prepare__(mcls, name, bases):
            return {}

    class BMeta(AMeta):

        def __new__(mcls, name, bases, ns):
            new_calls.append('BMeta')
            return super().__new__(mcls, name, bases, ns)

        @classmethod
        def __prepare__(mcls, name, bases):
            ns = super().__prepare__(name, bases)
            ns['BMeta_was_here'] = True
            return ns
    A = types.new_class('A', (), {'metaclass': AMeta})
    self.assertEqual(new_calls, ['AMeta'])
    new_calls.clear()
    B = types.new_class('B', (), {'metaclass': BMeta})
    self.assertEqual(new_calls, ['BMeta', 'AMeta'])
    new_calls.clear()
    C = types.new_class('C', (A, B))
    self.assertEqual(new_calls, ['BMeta', 'AMeta'])
    new_calls.clear()
    self.assertIn('BMeta_was_here', C.__dict__)
    C2 = types.new_class('C2', (B, A))
    self.assertEqual(new_calls, ['BMeta', 'AMeta'])
    new_calls.clear()
    self.assertIn('BMeta_was_here', C2.__dict__)
    D = types.new_class('D', (C,), {'metaclass': type})
    self.assertEqual(new_calls, ['BMeta', 'AMeta'])
    new_calls.clear()
    self.assertIn('BMeta_was_here', D.__dict__)
    E = types.new_class('E', (C,), {'metaclass': AMeta})
    self.assertEqual(new_calls, ['BMeta', 'AMeta'])
    new_calls.clear()
    self.assertIn('BMeta_was_here', E.__dict__)
