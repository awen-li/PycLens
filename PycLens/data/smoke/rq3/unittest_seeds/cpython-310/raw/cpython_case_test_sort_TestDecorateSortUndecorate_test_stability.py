# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestDecorateSortUndecorate_test_stability

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [(random.randrange(100), i) for i in range(200)]
    copy = data[:]
    data.sort(key=lambda t: t[0])
    copy.sort()
    self.assertEqual(data, copy)
