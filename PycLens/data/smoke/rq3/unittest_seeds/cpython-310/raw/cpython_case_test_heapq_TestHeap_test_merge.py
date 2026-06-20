# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_merge

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    inputs = []
    for i in range(random.randrange(25)):
        row = []
        for j in range(random.randrange(100)):
            tup = (random.choice('ABC'), random.randrange(-500, 500))
            row.append(tup)
        inputs.append(row)
    for key in [None, itemgetter(0), itemgetter(1), itemgetter(1, 0)]:
        for reverse in [False, True]:
            seqs = []
            for seq in inputs:
                seqs.append(sorted(seq, key=key, reverse=reverse))
            self.assertEqual(sorted(chain(*inputs), key=key, reverse=reverse), list(self.module.merge(*seqs, key=key, reverse=reverse)))
            self.assertEqual(list(self.module.merge()), [])
