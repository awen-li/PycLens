# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_MutableMapping_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mymap = UserDict()
    mymap['red'] = 5
    self.assertIsInstance(mymap.keys(), Set)
    self.assertIsInstance(mymap.keys(), KeysView)
    self.assertIsInstance(mymap.values(), Collection)
    self.assertIsInstance(mymap.values(), ValuesView)
    self.assertIsInstance(mymap.items(), Set)
    self.assertIsInstance(mymap.items(), ItemsView)
    mymap = UserDict()
    mymap['red'] = 5
    z = mymap.keys() | {'orange'}
    self.assertIsInstance(z, set)
    list(z)
    mymap['blue'] = 7
    self.assertEqual(sorted(z), ['orange', 'red'])
    mymap = UserDict()
    mymap['red'] = 5
    z = mymap.items() | {('orange', 3)}
    self.assertIsInstance(z, set)
    list(z)
    mymap['blue'] = 7
    self.assertEqual(z, {('orange', 3), ('red', 5)})
