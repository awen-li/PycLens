# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestBisect_test_lookups_with_key_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod = self.module
    keyfunc = abs
    arr = sorted([2, -4, 6, 8, -10], key=keyfunc)
    precomputed_arr = list(map(keyfunc, arr))
    for x in precomputed_arr:
        self.assertEqual(mod.bisect_left(arr, x, key=keyfunc), mod.bisect_left(precomputed_arr, x))
        self.assertEqual(mod.bisect_right(arr, x, key=keyfunc), mod.bisect_right(precomputed_arr, x))
    keyfunc = str.casefold
    arr = sorted('aBcDeEfgHhiIiij', key=keyfunc)
    precomputed_arr = list(map(keyfunc, arr))
    for x in precomputed_arr:
        self.assertEqual(mod.bisect_left(arr, x, key=keyfunc), mod.bisect_left(precomputed_arr, x))
        self.assertEqual(mod.bisect_right(arr, x, key=keyfunc), mod.bisect_right(precomputed_arr, x))
