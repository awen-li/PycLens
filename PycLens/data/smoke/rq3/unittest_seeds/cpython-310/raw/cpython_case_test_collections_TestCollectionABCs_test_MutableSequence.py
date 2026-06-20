# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_MutableSequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for sample in [tuple, str, bytes]:
        self.assertNotIsInstance(sample(), MutableSequence)
        self.assertFalse(issubclass(sample, MutableSequence))
    for sample in [list, bytearray, deque]:
        self.assertIsInstance(sample(), MutableSequence)
        self.assertTrue(issubclass(sample, MutableSequence))
    self.assertFalse(issubclass(str, MutableSequence))
    self.validate_abstract_methods(MutableSequence, '__contains__', '__iter__', '__len__', '__getitem__', '__setitem__', '__delitem__', 'insert')
