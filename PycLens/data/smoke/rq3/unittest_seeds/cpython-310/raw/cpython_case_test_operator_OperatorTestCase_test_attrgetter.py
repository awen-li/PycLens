# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_operator.py
# case: OperatorTestCase_test_attrgetter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    operator = self.module

    class A:
        pass
    a = A()
    a.name = 'arthur'
    f = operator.attrgetter('name')
    self.assertEqual(f(a), 'arthur')
    self.assertRaises(TypeError, f)
    self.assertRaises(TypeError, f, a, 'dent')
    self.assertRaises(TypeError, f, a, surname='dent')
    f = operator.attrgetter('rank')
    self.assertRaises(AttributeError, f, a)
    self.assertRaises(TypeError, operator.attrgetter, 2)
    self.assertRaises(TypeError, operator.attrgetter)
    record = A()
    record.x = 'X'
    record.y = 'Y'
    record.z = 'Z'
    self.assertEqual(operator.attrgetter('x', 'z', 'y')(record), ('X', 'Z', 'Y'))
    self.assertRaises(TypeError, operator.attrgetter, ('x', (), 'y'))

    class C(object):

        def __getattr__(self, name):
            raise SyntaxError
    self.assertRaises(SyntaxError, operator.attrgetter('foo'), C())
    a = A()
    a.name = 'arthur'
    a.child = A()
    a.child.name = 'thomas'
    f = operator.attrgetter('child.name')
    self.assertEqual(f(a), 'thomas')
    self.assertRaises(AttributeError, f, a.child)
    f = operator.attrgetter('name', 'child.name')
    self.assertEqual(f(a), ('arthur', 'thomas'))
    f = operator.attrgetter('name', 'child.name', 'child.child.name')
    self.assertRaises(AttributeError, f, a)
    f = operator.attrgetter('child.')
    self.assertRaises(AttributeError, f, a)
    f = operator.attrgetter('.child')
    self.assertRaises(AttributeError, f, a)
    a.child.child = A()
    a.child.child.name = 'johnson'
    f = operator.attrgetter('child.child.name')
    self.assertEqual(f(a), 'johnson')
    f = operator.attrgetter('name', 'child.name', 'child.child.name')
    self.assertEqual(f(a), ('arthur', 'thomas', 'johnson'))
