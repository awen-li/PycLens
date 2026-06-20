# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(start, stop, step=None):
        i = slice(start, stop, step)
        self.assertEqual(list(r[i]), list(r)[i])
        self.assertEqual(len(r[i]), len(list(r)[i]))
    for r in [range(10), range(0), range(1, 9, 3), range(8, 0, -3), range(sys.maxsize + 1, sys.maxsize + 10)]:
        check(0, 2)
        check(0, 20)
        check(1, 2)
        check(20, 30)
        check(-30, -20)
        check(-1, 100, 2)
        check(0, -1)
        check(-1, -3, -1)
