# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_heapq.py
# case: TestHeap_test_merge_does_not_suppress_index_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def iterable():
        s = list(range(10))
        for i in range(20):
            yield s[i]
    with self.assertRaises(IndexError):
        list(self.module.merge(iterable(), iterable()))
