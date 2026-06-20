# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_filter_dealloc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    max_iters = 1000000
    i = filter(bool, range(max_iters))
    for _ in range(max_iters):
        i = filter(bool, i)
    del i
    gc.collect()
