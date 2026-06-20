# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestExamples_test_accumulate_reducible

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [1, 2, 3, 4, 5]
    accumulated = [1, 3, 6, 10, 15]
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        it = accumulate(data)
        self.assertEqual(list(pickle.loads(pickle.dumps(it, proto))), accumulated[:])
        self.assertEqual(next(it), 1)
        self.assertEqual(list(pickle.loads(pickle.dumps(it, proto))), accumulated[1:])
    it = accumulate(data)
    self.assertEqual(next(it), 1)
    self.assertEqual(list(copy.deepcopy(it)), accumulated[1:])
    self.assertEqual(list(copy.copy(it)), accumulated[1:])
