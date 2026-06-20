# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_iterator_pickling_overflowing_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(proto=proto):
            it = iter(range(2 ** 32 + 2))
            (_, _, idx) = it.__reduce__()
            self.assertEqual(idx, 0)
            it.__setstate__(2 ** 32 + 1)
            (_, _, idx) = it.__reduce__()
            self.assertEqual(idx, 2 ** 32 + 1)
            d = pickle.dumps(it, proto)
            it = pickle.loads(d)
            self.assertEqual(next(it), 2 ** 32 + 1)
