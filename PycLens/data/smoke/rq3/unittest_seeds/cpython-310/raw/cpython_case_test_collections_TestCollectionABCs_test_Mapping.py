# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_Mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for sample in [dict]:
        self.assertIsInstance(sample(), Mapping)
        self.assertTrue(issubclass(sample, Mapping))
    self.validate_abstract_methods(Mapping, '__contains__', '__iter__', '__len__', '__getitem__')

    class MyMapping(Mapping):

        def __len__(self):
            return 0

        def __getitem__(self, i):
            raise IndexError

        def __iter__(self):
            return iter(())
    self.validate_comparison(MyMapping())
    self.assertRaises(TypeError, reversed, MyMapping())
