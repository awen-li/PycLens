# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_collection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(tuple(), typing.Collection)
    self.assertIsInstance(frozenset(), typing.Collection)
    self.assertIsSubclass(dict, typing.Collection)
    self.assertNotIsInstance(42, typing.Collection)
