# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_iter_independence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    seq = range(3)
    res = []
    for i in iter(seq):
        for j in iter(seq):
            for k in iter(seq):
                res.append((i, j, k))
    self.assertEqual(res, TRIPLETS)
