# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestDecorateSortUndecorate_test_reverse_stability

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [(random.randrange(100), i) for i in range(200)]
    copy1 = data[:]
    copy2 = data[:]

    def my_cmp(x, y):
        (x0, y0) = (x[0], y[0])
        return (x0 > y0) - (x0 < y0)

    def my_cmp_reversed(x, y):
        (x0, y0) = (x[0], y[0])
        return (y0 > x0) - (y0 < x0)
    data.sort(key=cmp_to_key(my_cmp), reverse=True)
    copy1.sort(key=cmp_to_key(my_cmp_reversed))
    self.assertEqual(data, copy1)
    copy2.sort(key=lambda x: x[0], reverse=True)
    self.assertEqual(data, copy2)
