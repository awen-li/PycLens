# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_MutableMapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for sample in [dict]:
        self.assertIsInstance(sample(), MutableMapping)
        self.assertTrue(issubclass(sample, MutableMapping))
    self.validate_abstract_methods(MutableMapping, '__contains__', '__iter__', '__len__', '__getitem__', '__setitem__', '__delitem__')
