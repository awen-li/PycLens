# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NamedTupleTests_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Emp = NamedTuple('Emp', [('name', str), ('id', int)])
    self.assertIsSubclass(Emp, tuple)
    joe = Emp('Joe', 42)
    jim = Emp(name='Jim', id=1)
    self.assertIsInstance(joe, Emp)
    self.assertIsInstance(joe, tuple)
    self.assertEqual(joe.name, 'Joe')
    self.assertEqual(joe.id, 42)
    self.assertEqual(jim.name, 'Jim')
    self.assertEqual(jim.id, 1)
    self.assertEqual(Emp.__name__, 'Emp')
    self.assertEqual(Emp._fields, ('name', 'id'))
    self.assertEqual(Emp.__annotations__, collections.OrderedDict([('name', str), ('id', int)]))
