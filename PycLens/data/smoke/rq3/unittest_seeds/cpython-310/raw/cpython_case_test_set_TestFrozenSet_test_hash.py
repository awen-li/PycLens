# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestFrozenSet_test_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(hash(self.thetype('abcdeb')), hash(self.thetype('ebecda')))
    n = 100
    seq = [randrange(n) for i in range(n)]
    results = set()
    for i in range(200):
        shuffle(seq)
        results.add(hash(self.thetype(seq)))
    self.assertEqual(len(results), 1)
