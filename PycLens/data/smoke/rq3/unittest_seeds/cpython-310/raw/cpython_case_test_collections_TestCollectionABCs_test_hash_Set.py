# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_hash_Set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class OneTwoThreeSet(Set):

        def __init__(self):
            self.contents = [1, 2, 3]

        def __contains__(self, x):
            return x in self.contents

        def __len__(self):
            return len(self.contents)

        def __iter__(self):
            return iter(self.contents)

        def __hash__(self):
            return self._hash()
    (a, b) = (OneTwoThreeSet(), OneTwoThreeSet())
    self.assertTrue(hash(a) == hash(b))
