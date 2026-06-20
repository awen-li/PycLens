# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestGC_test_issue2246

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 10
    keyfunc = lambda x: x
    for (i, j) in groupby(range(n), key=keyfunc):
        keyfunc.__dict__.setdefault('x', []).append(j)
