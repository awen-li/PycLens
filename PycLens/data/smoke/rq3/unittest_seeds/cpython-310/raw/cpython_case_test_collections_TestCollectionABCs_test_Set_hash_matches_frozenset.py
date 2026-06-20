# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_Set_hash_matches_frozenset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sets = [{}, {1}, {None}, {-1}, {0.0}, {'abc'}, {1, 2, 3}, {10 ** 100, 10 ** 101}, {'a', 'b', 'ab', ''}, {False, True}, {object(), object(), object()}, {float('nan')}, {frozenset()}, {*range(1000)}, {*range(1000)} - {100, 200, 300}, {*range(sys.maxsize - 10, sys.maxsize + 10)}]
    for s in sets:
        fs = frozenset(s)
        self.assertEqual(hash(fs), Set._hash(fs), msg=s)
