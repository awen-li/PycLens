# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_issue8750

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    empty = WithSet()
    full = WithSet(range(10))
    s = WithSet(full)
    s -= s
    self.assertEqual(s, empty)
    s = WithSet(full)
    s ^= s
    self.assertEqual(s, empty)
    s = WithSet(full)
    s &= s
    self.assertEqual(s, full)
    s |= s
    self.assertEqual(s, full)
