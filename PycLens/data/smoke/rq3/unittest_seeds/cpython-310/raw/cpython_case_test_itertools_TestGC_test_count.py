# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestGC_test_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = []
    Int = type('Int', (int,), dict(x=a))
    self.makecycle(count(Int(0), Int(1)), a)
