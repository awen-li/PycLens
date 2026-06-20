# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_hashable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(42, typing.Hashable)
    self.assertNotIsInstance([], typing.Hashable)
