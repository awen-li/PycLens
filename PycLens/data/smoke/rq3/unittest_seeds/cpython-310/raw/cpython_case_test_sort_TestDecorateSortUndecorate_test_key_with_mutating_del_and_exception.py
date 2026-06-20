# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestDecorateSortUndecorate_test_key_with_mutating_del_and_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = list(range(10))

    class SortKiller(object):

        def __init__(self, x):
            if x > 2:
                raise RuntimeError

        def __del__(self):
            del data[:]
            data[:] = list(range(20))
    self.assertRaises(RuntimeError, data.sort, key=SortKiller)
