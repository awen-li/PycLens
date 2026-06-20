# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_Sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for sample in [tuple, list, bytes, str]:
        self.assertIsInstance(sample(), Sequence)
        self.assertTrue(issubclass(sample, Sequence))
    self.assertIsInstance(range(10), Sequence)
    self.assertTrue(issubclass(range, Sequence))
    self.assertIsInstance(memoryview(b''), Sequence)
    self.assertTrue(issubclass(memoryview, Sequence))
    self.assertTrue(issubclass(str, Sequence))
    self.validate_abstract_methods(Sequence, '__contains__', '__iter__', '__len__', '__getitem__')
