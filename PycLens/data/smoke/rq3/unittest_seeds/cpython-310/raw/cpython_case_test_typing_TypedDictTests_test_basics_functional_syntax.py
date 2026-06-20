# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_basics_functional_syntax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Emp = TypedDict('Emp', {'name': str, 'id': int})
    self.assertIsSubclass(Emp, dict)
    self.assertIsSubclass(Emp, typing.MutableMapping)
    self.assertNotIsSubclass(Emp, collections.abc.Sequence)
    jim = Emp(name='Jim', id=1)
    self.assertIs(type(jim), dict)
    self.assertEqual(jim['name'], 'Jim')
    self.assertEqual(jim['id'], 1)
    self.assertEqual(Emp.__name__, 'Emp')
    self.assertEqual(Emp.__module__, __name__)
    self.assertEqual(Emp.__bases__, (dict,))
    self.assertEqual(Emp.__annotations__, {'name': str, 'id': int})
    self.assertEqual(Emp.__total__, True)
