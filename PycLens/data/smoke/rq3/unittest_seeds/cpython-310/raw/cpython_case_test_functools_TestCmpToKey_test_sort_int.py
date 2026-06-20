# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCmpToKey_test_sort_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def mycmp(x, y):
        return y - x
    self.assertEqual(sorted(range(5), key=self.cmp_to_key(mycmp)), [4, 3, 2, 1, 0])
