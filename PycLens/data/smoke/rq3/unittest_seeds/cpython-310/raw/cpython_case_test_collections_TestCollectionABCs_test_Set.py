# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_Set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for sample in [set, frozenset]:
        self.assertIsInstance(sample(), Set)
        self.assertTrue(issubclass(sample, Set))
    self.validate_abstract_methods(Set, '__contains__', '__iter__', '__len__')

    class MySet(Set):

        def __contains__(self, x):
            return False

        def __len__(self):
            return 0

        def __iter__(self):
            return iter([])
    self.validate_comparison(MySet())
