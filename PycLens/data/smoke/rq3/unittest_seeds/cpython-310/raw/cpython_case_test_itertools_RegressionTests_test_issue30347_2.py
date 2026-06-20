# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: RegressionTests_test_issue30347_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class K:

        def __init__(self, v):
            pass

        def __eq__(self, other):
            nonlocal i
            i += 1
            if i == 1:
                next(g, None)
            return True
    i = 0
    g = next(groupby(range(10), K))[1]
    for j in range(2):
        next(g, None)
