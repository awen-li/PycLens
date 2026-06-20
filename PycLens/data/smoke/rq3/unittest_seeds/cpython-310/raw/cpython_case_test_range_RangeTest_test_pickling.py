# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    testcases = [(13,), (0, 11), (-22, 10), (20, 3, -1), (13, 21, 3), (-2, 2, 2), (2 ** 65, 2 ** 65 + 2)]
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        for t in testcases:
            with self.subTest(proto=proto, test=t):
                r = range(*t)
                self.assertEqual(list(pickle.loads(pickle.dumps(r, proto))), list(r))
