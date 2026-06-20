# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: RegressionTests_test_issue30347_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(n):
        if n == 5:
            list(b)
        return n != 6
    for (k, b) in groupby(range(10), f):
        list(b)
