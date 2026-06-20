# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_arithmetic_Set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MySet(Set):

        def __init__(self, itr):
            self.contents = itr

        def __contains__(self, x):
            return x in self.contents

        def __iter__(self):
            return iter(self.contents)

        def __len__(self):
            return len([x for x in self.contents])
    s1 = MySet((1, 2, 3))
    s2 = MySet((3, 4, 5))
    s3 = s1 & s2
    self.assertEqual(s3, MySet((3,)))
