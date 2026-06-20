# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_issue11845

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = range(*slice(1, 18, 2).indices(20))
    values = {None, 0, 1, -1, 2, -2, 5, -5, 19, -19, 20, -20, 21, -21, 30, -30, 99, -99}
    for i in values:
        for j in values:
            for k in values - {0}:
                r[i:j:k]
