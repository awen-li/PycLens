# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_large_exhausted_iterator_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        r = range(20)
        i = iter(r)
        while True:
            r = next(i)
            if r == 19:
                break
        d = pickle.dumps(i, proto)
        i2 = pickle.loads(d)
        self.assertEqual(list(i), [])
        self.assertEqual(list(i2), [])
