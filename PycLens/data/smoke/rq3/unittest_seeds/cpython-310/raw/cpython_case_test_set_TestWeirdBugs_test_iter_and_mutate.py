# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestWeirdBugs_test_iter_and_mutate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = set(range(100))
    s.clear()
    s.update(range(100))
    si = iter(s)
    s.clear()
    a = list(range(100))
    s.update(range(100))
    list(si)
