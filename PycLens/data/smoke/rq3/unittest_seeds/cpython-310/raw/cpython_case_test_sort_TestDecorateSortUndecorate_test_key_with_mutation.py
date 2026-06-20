# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestDecorateSortUndecorate_test_key_with_mutation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = list(range(10))

    def k(x):
        del data[:]
        data[:] = range(20)
        return x
    self.assertRaises(ValueError, data.sort, key=k)
