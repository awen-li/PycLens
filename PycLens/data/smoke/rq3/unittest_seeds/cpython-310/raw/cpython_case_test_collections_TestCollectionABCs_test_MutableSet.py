# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_MutableSet

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(set(), MutableSet)
    self.assertTrue(issubclass(set, MutableSet))
    self.assertNotIsInstance(frozenset(), MutableSet)
    self.assertFalse(issubclass(frozenset, MutableSet))
    self.validate_abstract_methods(MutableSet, '__contains__', '__iter__', '__len__', 'add', 'discard')
