# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_iterator_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testcases = [(13,), (0, 11), (-22, 10), (20, 3, -1), (13, 21, 3), (-2, 2, 2)]
    for M in (2 ** 31, 2 ** 63):
        testcases += [(M - 3, M - 1), (4 * M, 4 * M + 2), (M - 2, M - 1, 2), (-M + 1, -M, -2), (1, 2, M - 1), (-1, -2, -M), (1, M - 1, M - 1), (-1, -M, -M)]
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        for t in testcases:
            with self.subTest(proto=proto, t=t):
                it = itorg = iter(range(*t))
                data = list(range(*t))
                d = pickle.dumps(it, proto)
                it = pickle.loads(d)
                self.assertEqual(type(itorg), type(it))
                self.assertEqual(list(it), data)
                it = pickle.loads(d)
                try:
                    next(it)
                except StopIteration:
                    continue
                d = pickle.dumps(it, proto)
                it = pickle.loads(d)
                self.assertEqual(list(it), data[1:])
