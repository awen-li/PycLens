# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCmpToKey_test_sort_int_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def mycmp(x, y):
        (x, y) = (int(x), int(y))
        return (x > y) - (x < y)
    values = [5, '3', 7, 2, '0', '1', 4, '10', 1]
    values = sorted(values, key=self.cmp_to_key(mycmp))
    self.assertEqual([int(value) for value in values], [0, 1, 1, 2, 3, 4, 5, 7, 10])
