# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_reverse_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for r in [range(10), range(0), range(1, 9, 3), range(8, 0, -3), range(sys.maxsize + 1, sys.maxsize + 10)]:
        self.assertEqual(list(reversed(r)), list(r)[::-1])
