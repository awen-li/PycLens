# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_issue16373

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyComparableSet(Set):

        def __contains__(self, x):
            return False

        def __len__(self):
            return 0

        def __iter__(self):
            return iter([])

    class MyNonComparableSet(Set):

        def __contains__(self, x):
            return False

        def __len__(self):
            return 0

        def __iter__(self):
            return iter([])

        def __le__(self, x):
            return NotImplemented

        def __lt__(self, x):
            return NotImplemented
    cs = MyComparableSet()
    ncs = MyNonComparableSet()
    self.assertFalse(ncs < cs)
    self.assertTrue(ncs <= cs)
    self.assertFalse(ncs > cs)
    self.assertTrue(ncs >= cs)
