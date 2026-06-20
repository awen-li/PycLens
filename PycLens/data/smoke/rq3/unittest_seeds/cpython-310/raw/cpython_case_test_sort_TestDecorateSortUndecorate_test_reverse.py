# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestDecorateSortUndecorate_test_reverse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = list(range(100))
    random.shuffle(data)
    data.sort(reverse=True)
    self.assertEqual(data, list(range(99, -1, -1)))
